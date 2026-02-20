import BERT_models
import diagnoses
import prompts_HAPA
import tokens

experiments = [
    # BERT_base, EN, MH
    {
        "model": BERT_models.BERT_base,
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
        "model": BERT_models.BERT_base,
        "model_name": "BERT_base",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DisorBERT, EN, MH
    {
        "model": BERT_models.DisorBERT,
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
        "model": BERT_models.DisorBERT,
        "model_name": "DisorBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DepBERT, EN, MH
    {
        "model": BERT_models.DepBERT,
        "model_name": "DepBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DepBERT, EN, non_MH
    {
        "model": BERT_models.DepBERT,
        "model_name": "DepBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # SHBERT, EN, MH
    {
        "model": BERT_models.SHBERT,
        "model_name": "SHBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # SHBERT, EN, non_MH
    {
        "model": BERT_models.SHBERT,
        "model_name": "SHBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # GambBERT, EN, MH
    {
        "model": BERT_models.GambBERT,
        "model_name": "GambBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # GambBERT, EN, non_MH
    {
        "model": BERT_models.GambBERT,
        "model_name": "GambBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # AnorBERT, EN, MH
    {
        "model": BERT_models.AnorBERT,
        "model_name": "AnorBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # AnorBERT, EN, non_MH
    {
        "model": BERT_models.AnorBERT,
        "model_name": "AnorBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # WholeBERT, EN, MH
    {
        "model": BERT_models.WholeBERT,
        "model_name": "WholeBERT",
        "language": "EN",
        "health_type": "MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # WholeBERT, EN, non_MH
    {
        "model": BERT_models.WholeBERT,
        "model_name": "WholeBERT",
        "language": "EN",
        "health_type": "non_MH",
        "male_tokens": tokens.male_EN,
        "female_tokens": tokens.female_EN,
        "proper_nouns_csv": "../proper nouns/proper_nouns_EN.csv",
        "diagnoses": diagnoses.non_MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    }
]