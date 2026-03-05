import torch
import gc
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import experiments_matrix
import evaluators

# Quantization settings for consumer GPUs (RTX 2060)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

experiments = experiments_matrix.experiments

for exp in experiments:

    print(f"{exp['model_name']}_{exp['language']}_{exp['health_type']}")

    # Model and Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(exp['model'])
    model = AutoModelForCausalLM.from_pretrained(
        exp['model'],
        device_map="auto",
        quantization_config=bnb_config
    )

    # Evaluators
    results = evaluators.LLM_bias_per_diagnosis(
        model=model,
        tokenizer=tokenizer,
        diagnoses=exp["diagnoses"],
        templates=exp["templates"],
        language=exp["language"]
    )

    # 3. Save
    results.to_csv(
        f"../results/{exp['model_name']}_{exp['language']}_{exp['health_type']}.csv",
        index=True,
        encoding='utf-8'
    )

    # VRAM Cleaning
    del model
    del tokenizer
    torch.cuda.empty_cache()
    gc.collect()