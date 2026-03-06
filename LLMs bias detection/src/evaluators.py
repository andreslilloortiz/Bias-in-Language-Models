import pandas as pd # type: ignore
from tqdm import tqdm
import ollama

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

def LLM_bias_per_diagnosis(model, diagnoses, templates, language):
    results = []

    for phase, sentences in templates.items():
        for template in sentences:
            for diag in tqdm(diagnoses, desc=f"Evaluating {phase}"):

                prompt = template.format(diagnosis=diag)

                try:
                    response = ollama.generate(
                        model=model,
                        prompt=prompt,
                        options={
                            "temperature": 0.01,
                            "num_predict": 10
                        }
                    )

                    raw_output = response['response'].strip()
                    prediction = clean_generative_response(raw_output, language)

                except Exception as e:
                    print(f"\n[!] Ollama error in '{diag}': {e}")
                    raw_output = "OLLAMA_ERROR"
                    prediction = "Indeterminated"

                metrics = {
                    "phase": phase,
                    "diagnosis": diag,
                    "prompt": prompt,
                    "raw_output": raw_output,
                    "prediction": prediction
                }
                results.append(metrics)

    return pd.DataFrame(results)