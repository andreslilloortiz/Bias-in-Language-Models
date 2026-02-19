import models
import diagnoses
import prompts_HAPA
import tokens

experiments = [
    # DisorBERT, EN, MH
    {
        "model": models.DisorBERT,
        "model_name": "DisorBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DisorBERT, EN, non_MH
    {
        "model": models.DisorBERT,
        "model_name": "DisorBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # BERT_base, EN, MH
    {
        "model": models.BERT_base,
        "model_name": "BERT_base",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # BERT_base, EN, non_MH
    {
        "model": models.BERT_base,
        "model_name": "BERT_base",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    }
]