import models
import diagnoses
import prompts_HAPA

experiments = [
    # Salamandra, ES, MH
    {
        "model": models.Salamandra,
        "model_name": "Salamandra",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Llama3, EN, MH
    {
        "model": models.Llama3,
        "model_name": "Llama3",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # MentaLLaMA, EN, MH
    {
        "model": models.MentaLLaMA,
        "model_name": "MentaLLaMA",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    }
]