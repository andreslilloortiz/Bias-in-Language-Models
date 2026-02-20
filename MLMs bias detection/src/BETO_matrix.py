import BETO_models
import diagnoses
import prompts_HAPA
import tokens

experiments = [
    # BETO, ES, MH
    {
        "model": BETO_models.BETO,
        "model_name": "BETO",
        "language": "ES",
        "health_type": "MH",
        "male_tokens": tokens.male_ES,
        "female_tokens": tokens.female_ES,
        "proper_nouns_csv": "../proper nouns/proper_nouns_ES.csv",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # BETO, ES, non_MH
    {
        "model": BETO_models.BETO,
        "model_name": "BETO",
        "language": "ES",
        "health_type": "non_MH",
        "male_tokens": tokens.male_ES,
        "female_tokens": tokens.female_ES,
        "proper_nouns_csv": "../proper nouns/proper_nouns_ES.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # ludoBETO, ES, MH
    {
        "model": BETO_models.ludoBETO,
        "model_name": "ludoBETO",
        "language": "ES",
        "health_type": "MH",
        "male_tokens": tokens.male_ES,
        "female_tokens": tokens.female_ES,
        "proper_nouns_csv": "../proper nouns/proper_nouns_ES.csv",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # ludoBETO, ES, non_MH
    {
        "model": BETO_models.ludoBETO,
        "model_name": "ludoBETO",
        "language": "ES",
        "health_type": "non_MH",
        "male_tokens": tokens.male_ES,
        "female_tokens": tokens.female_ES,
        "proper_nouns_csv": "../proper nouns/proper_nouns_ES.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    }
]