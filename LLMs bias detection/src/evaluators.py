import pandas as pd # type: ignore
from tqdm import tqdm

def clean_generative_response(text, language):
    """Clean up the model's verbiage and force a binary label"""
    text = text.lower()
    if language == "ES":
        if "mujer" in text: return "female"
        elif "hombre" in text: return "male"
    elif language == "EN":
        if "woman" in text or "female" in text: return "female"
        elif "man" in text or "male" in text: return "male"
    return "unspecified"

def LLM_bias_per_diagnosis(model, tokenizer, diagnoses, templates, language):
    results = []

    for phase, sentences in templates.items():
        for template in sentences:
            for diag in tqdm(diagnoses, desc=f"Evaluating {phase}"):

                prompt = template.format(diagnosis=diag)
                inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

                outputs = model.generate(
                    **inputs,
                    max_new_tokens=15,
                    temperature=0.1,
                    do_sample=True,
                    pad_token_id=tokenizer.eos_token_id
                )

                full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                split_keyword = "Respuesta:" if language == "ES" else "Answer:"
                raw_output = full_response.split(split_keyword)[-1].strip()

                prediction = clean_generative_response(raw_output, language)

                metrics = {
                    "phase": phase,
                    "diagnosis": diag,
                    "prompt": prompt,
                    "raw_output": raw_output,
                    "prediction": prediction
                }
                results.append(metrics)

    return pd.DataFrame(results)