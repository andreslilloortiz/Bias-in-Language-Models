import models
import diagnoses
import prompts_HAPA
import tokens

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