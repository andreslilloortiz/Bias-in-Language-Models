import pandas as pd # type: ignore
from tqdm import tqdm # type: ignore
import ollama # type: ignore

def LLM_bias_per_diagnosis(model, diagnoses, templates):
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
                        }
                    )

                    raw_output = response['response'].strip()

                except Exception as e:
                    print(f"\n[!] Ollama error in '{diag}': {e}")
                    raw_output = "OLLAMA_ERROR"

                metrics = {
                    "phase": phase,
                    "diagnosis": diag,
                    "prompt": prompt,
                    "raw_output": raw_output
                }
                results.append(metrics)

    return pd.DataFrame(results)