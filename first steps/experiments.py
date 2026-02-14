import pandas as pd # type: ignore
import unicodedata

def _normalize_token(token):
    token = token.strip().lower()
    token = unicodedata.normalize('NFD', token)
    token = "".join(c for c in token if not unicodedata.combining(c))
    return token

def _load_token_vocabularies(male_tokens, female_tokens, proper_nouns_csv):

    proper_nouns = pd.read_csv(proper_nouns_csv)
    proper_nouns_male = [_normalize_token(token) for token in proper_nouns[proper_nouns['Gender'] == 'male']['Name']]
    proper_nouns_female = [_normalize_token(token) for token in proper_nouns[proper_nouns['Gender'] == 'female']['Name']]

    male_set = set(proper_nouns_male + [_normalize_token(token) for token in male_tokens])
    female_set = set(proper_nouns_female + [_normalize_token(token) for token in female_tokens])

    return male_set, female_set

def RQ1_2210_15144v2(filler, diagnoses, templates, male_tokens, female_tokens, proper_nouns_csv):

    results = []

    male_vocabularie, female_vocabularie = _load_token_vocabularies(male_tokens, female_tokens, proper_nouns_csv)

    for phase, sentences in templates.items():
        for template in sentences:
            for diag in diagnoses:

                prompt = template.replace("[diagnosis]", diag).replace("<mask>", filler.tokenizer.mask_token)

                predictions = filler(prompt, top_k = 50)

                metrics = {
                    "phase": phase,
                    "diagnosis": diag,
                    "p_female": 0.0,
                    "p_male": 0.0,
                    "p_unspecified": 0.0,
                    "tokens_female": [],
                    "tokens_male": [],
                    "tokens_unspecified": []
                }

                for pred in predictions:
                    score = pred['score']
                    token = _normalize_token(pred['token_str'])

                    if score < 0.01:
                        continue

                    if token in female_vocabularie:
                        metrics["p_female"] += score
                        metrics["tokens_female"].append(f"{token} ({score:.4f})")
                    elif token in male_vocabularie:
                        metrics["p_male"] += score
                        metrics["tokens_male"].append(f"{token} ({score:.4f})")
                    else:
                        metrics["p_unspecified"] += score
                        metrics["tokens_unspecified"].append(f"{token} ({score:.4f})")

                results.append(metrics)

    return pd.DataFrame(results)

if __name__ == "__main__":
    pass