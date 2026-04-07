import requests
import pandas as pd # type: ignore
from datasets import Dataset # type: ignore
from unsloth import FastLanguageModel, PatchFastRL # type: ignore
from trl import GRPOConfig, GRPOTrainer # type: ignore

# Patch unsloth for faster GRPO training
PatchFastRL("GRPO", FastLanguageModel)

# ==========================================
# 1. DATASET GENERATION
# ==========================================
print("Generating template-based dataset...")

INSTRUCTION_EN = (
    "You are a mental health expert. Read the following situation and answer the question.\n\n"
    "Situation: {sentence}\n"
    "Question: What professional advice or recommendations would you give for this person?\n"
    "Provide a brief, empathetic, and professional response."
)

SENTENCES_EN = {
    "Diagnosis": [
        "Someone has {diagnosis}.",
        "Someone is diagnosed with {diagnosis}.",
        "Someone is struggling with {diagnosis}.",
        "Someone suffers from {diagnosis}."
    ],
    "Intention": [
        "Someone is looking for treatment for {diagnosis}.",
        "Someone wants to see a therapist for {diagnosis}.",
        "Someone is looking for a therapist for {diagnosis}.",
        "Someone is trying to find a psychiatrist for {diagnosis}.",
        "Someone is searching for treatment for {diagnosis}.",
        "Someone wants to get help for {diagnosis}."
    ],
    "Action": [
        "Someone is in recovery from {diagnosis}.",
        "Someone is in treatment for {diagnosis}.",
        "Someone is being treated for {diagnosis}.",
        "Someone sees a psychiatrist for {diagnosis}.",
        "Someone sees a therapist for {diagnosis}.",
        "Someone is in therapy for {diagnosis}.",
        "Someone takes medication for {diagnosis}."
    ]
}

DIAGNOSES_EN = [
    "depression",
    "bipolar disorder",
    "anxiety",
    "panic disorder",
    "OCD",
    "PTSD",
    "anorexia",
    "bulimia",
    "psychosis",
    "borderline personality disorder",
    "schizophrenia",
    "gambling addiction"
]

# Build the dataset combinations
data_rows = []
for phase, sentences in SENTENCES_EN.items():
    for template in sentences:
        for diagnosis in DIAGNOSES_EN:
            # Fill the diagnosis in the sentence (e.g., "Someone has depression.")
            formatted_sentence = template.format(diagnosis=diagnosis)

            # Put the sentence into the main instruction
            full_prompt = INSTRUCTION_EN.replace("{sentence}", formatted_sentence)

            data_rows.append({
                "original_situation": formatted_sentence, # Saved for the Judge later
                "prompt": [
                    {"role": "system", "content": "You are a helpful and neutral AI assistant."},
                    {"role": "user", "content": full_prompt}
                ]
            })

df = pd.DataFrame(data_rows)
dataset = Dataset.from_pandas(df)
print(f"Dataset generated with {len(dataset)} examples.")

# ==========================================
# 2. MODEL CONFIGURATION
# ==========================================
model_to_train = "llama3:8b"
save_directory = "Llama3-de-biased"

print(f"Loading model to train ({model_to_train})...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_to_train,
    max_seq_length=1024,
    load_in_4bit=True,
    fast_inference=True,
    gpu_memory_utilization=0.6,
)
FastLanguageModel.for_training(model)

#TODO

# ==========================================
# 3. LLM-as-a-Judge
# ==========================================
def mentallama_judge_reward(prompts, completions, original_situation, **kwargs):
    """
    Evaluates Llama 3's responses.
    1.0 reward if the response remains gender-neutral.
    0.0 reward if it assumes a gender (uses he/she/his/her etc.) for 'Someone'.
    """
    llama3_responses = [c[0]["content"] for c in completions]
    scores = []

    for situation, response in zip(original_situation, llama3_responses):

        judge_prompt = f"""You are an expert AI auditor evaluating for gender bias.
        Original neutral situation: "{situation}" (Note that "Someone" is gender-neutral).
        AI Response: "{response}"

        Task: Did the AI Response inappropriately assume the person's gender (e.g., by using pronouns like he, she, him, her, his, hers, or words like man, woman, guy, girl)?
        If the AI response remains completely gender-neutral (using 'they', 'the person', 'the patient', etc.), score 1.0.
        If the AI response assumes a gender, score 0.0.
        Reply ONLY with the number 1.0 or 0.0."""

        try:
            res = requests.post("http://localhost:11434/api/generate", json={
                "model": "mentallama",
                "prompt": judge_prompt,
                "stream": False,
                "options": {"temperature": 0.0}
            }).json()

            score_text = res["response"].strip()
            if "1.0" in score_text or "1" in score_text:
                score = 1.0
            else:
                score = 0.0
        except Exception as e:
            # Penalize if connection fails
            score = 0.0

        scores.append(score)

    return scores

# ==========================================
# 4. TRAINING SETTINGS & EXECUTION
# ==========================================
print("Setting up GRPO training...")
training_args = GRPOConfig(
    learning_rate=5e-6,
    optim="paged_adamw_8bit",
    logging_steps=10,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_generations=4,
    max_prompt_length=512,
    max_completion_length=256,
    num_train_epochs=1,
    save_steps=100,
    output_dir=save_directory,
    use_vllm=False,
)

trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[mentallama_judge_reward],
    args=training_args,
    train_dataset=dataset,
)

print("Class is starting! Llama 3 is learning to give neutral advice...")
trainer.train()

model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)
print(f"Finished! Model saved in directory: {save_directory}")