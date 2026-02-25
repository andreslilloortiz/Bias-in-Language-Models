import RoBERTa_models
import diagnoses
import prompts_HAPA
import tokens

experiments = [
    # RoBERTa_base, EN, MH
    {
        "model": RoBERTa_models.RoBERTa_base,
        "model_name": "RoBERTa_base",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # RoBERTa_base, EN, non_MH
    {
        "model": RoBERTa_models.RoBERTa_base,
        "model_name": "RoBERTa_base",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DisorRoBERTa, EN, MH
    {
        "model": RoBERTa_models.DisorRoBERTa,
        "model_name": "DisorRoBERTa",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DisorRoBERTa, EN, non_MH
    {
        "model": RoBERTa_models.DisorRoBERTa,
        "model_name": "DisorRoBERTa",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DepRoBERTa, EN, MH
    {
        "model": RoBERTa_models.DepRoBERTa,
        "model_name": "DepRoBERTa",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DepRoBERTa, EN, non_MH
    {
        "model": RoBERTa_models.DepRoBERTa,
        "model_name": "DepRoBERTa",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # SHRoBERTa, EN, MH
    {
        "model": RoBERTa_models.SHRoBERTa,
        "model_name": "SHRoBERTa",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # SHRoBERTa, EN, non_MH
    {
        "model": RoBERTa_models.SHRoBERTa,
        "model_name": "SHRoBERTa",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # GambRoBERTa, EN, MH
    {
        "model": RoBERTa_models.GambRoBERTa,
        "model_name": "GambRoBERTa",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # GambRoBERTa, EN, non_MH
    {
        "model": RoBERTa_models.GambRoBERTa,
        "model_name": "GambRoBERTa",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # AnorRoBERTa, EN, MH
    {
        "model": RoBERTa_models.AnorRoBERTa,
        "model_name": "AnorRoBERTa",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # AnorRoBERTa, EN, non_MH
    {
        "model": RoBERTa_models.AnorRoBERTa,
        "model_name": "AnorRoBERTa",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
]