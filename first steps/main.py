from transformers import pipeline # type: ignore
from datetime import datetime
import config
import models
import evaluators
import diagnoses
import prompts_HAPA
import vocabulary_utils
import tokens

# Experiment Matrix
experiments = [
    {
        "model": models.DisorBERT,
        "model_name": "DisorBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    {
        "model": models.DisorBERT,
        "model_name": "DisorBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    }
]

for exp in experiments:

    print(f"{exp["model_name"]}_{exp["language"]}_{exp["health_type"]}")

    # Pipeline
    filler = pipeline(
        "fill-mask",
        model = exp["model"],
        device = config.device
    )

    # Token vocabulary
    male_vocabulary, female_vocabulary= vocabulary_utils.load_token_vocabularies(
        male_tokens = exp["male_tokens"],
        female_tokens = exp["female_tokens"],
        proper_nouns_csv = exp["proper_nouns_csv"]
    )

    # Evaluators
    results = evaluators.RQ1_2210_15144v2(
        filler = filler,
        diagnoses = exp["diagnoses"],
        templates = exp["templates"],
        female_vocabulary = female_vocabulary,
        male_vocabulary = male_vocabulary
    )

    # Results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    results.to_csv(
        f"results/{exp['model_name']}_{exp['language']}_{exp['health_type']}_{timestamp}.csv",
        index = True,
        encoding = 'utf-8'
    )