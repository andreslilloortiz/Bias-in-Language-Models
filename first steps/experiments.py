import pandas as pd # type: ignore
import unicodedata

FEMALE_WORDS = {} #TODO
MALE_WORDS = {} #TODO

def normalize_token(token):
    token = token.strip().lower()
    token = unicodedata.normalize('NFD', token)
    token = "".join(c for c in token if not unicodedata.combining(c))
    return token

def RQ1_2210_15144v2(filler, diagnoses, templates):

    results = []

    for phase, template in templates.items():
        for diag in diagnoses:

            prompt = template.replace("[diagnosis]", diag).replace("<mask >", filler.tokenizer.mask_token)

            predictions = filler(prompt, top_k = 50)

            metrics = {
                "phase": phase,
                "diagnosis": diag,
                "p_female": 0.0,
                "p_male": 0.0,
                "tokens_female": [],
                "tokens_male": []
            }

            for pred in predictions:
                score = pred['score']
                token = normalize_token(pred['token_str'])

                if score < 0.01:
                    continue

                if token in FEMALE_WORDS:
                    metrics["p_female"] += score
                    metrics["tokens_female"].append(f"{token} ({score:.4f})")
                elif token in MALE_WORDS:
                    metrics["p_male"] += score
                    metrics["tokens_male"].append(f"{token} ({score:.4f})")

            results.append(metrics)

    return pd.DataFrame(results)