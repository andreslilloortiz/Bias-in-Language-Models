import pandas as pd # type: ignore
import vocabulary_utils

def RQ1_2210_15144v2(filler, diagnoses, templates, female_vocabulary, male_vocabulary):

    results = []

    for phase, sentences in templates.items():
        for template in sentences:
            for diag in diagnoses:

                prompt = template.replace("[diagnosis]", diag).replace("<mask>", filler.tokenizer.mask_token)

                predictions = filler(prompt, top_k = 300)

                metrics = {
                    "phase": phase,
                    "diagnosis": diag,
                    "prompt": prompt,
                    "p_female": 0.0,
                    "p_male": 0.0,
                    "p_unspecified": 0.0,
                    "tokens_female": [],
                    "tokens_male": [],
                    "tokens_unspecified": []
                }

                for pred in predictions:
                    score = pred['score']
                    token = vocabulary_utils.normalize_token(pred['token_str'])

                    # if score < 0.01:
                    #     continue

                    if token in female_vocabulary:
                        metrics["p_female"] += score
                        metrics["tokens_female"].append(f"{token} ({score:.4f})")
                    elif token in male_vocabulary:
                        metrics["p_male"] += score
                        metrics["tokens_male"].append(f"{token} ({score:.4f})")
                    else:
                        metrics["p_unspecified"] += score
                        metrics["tokens_unspecified"].append(f"{token} ({score:.4f})")

                results.append(metrics)

    return pd.DataFrame(results)

if __name__ == "__main__":
    pass