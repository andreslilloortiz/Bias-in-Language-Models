import models
import diagnoses
import prompts_HAPA

experiments = [
    # Llama_3, EN, MH
    {
        "model": models.Llama_3,
        "model_name": "Llama_3",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # Llama_3, ES, MH
    {
        "model": models.Llama_3,
        "model_name": "Llama_3",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Mistral, EN, MH
    {
        "model": models.Mistral,
        "model_name": "Mistral",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # Mistral, ES, MH
    {
        "model": models.Mistral,
        "model_name": "Mistral",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # DeepSeek, EN, MH
    {
        "model": models.DeepSeek,
        "model_name": "DeepSeek",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # DeepSeek, ES, MH
    {
        "model": models.DeepSeek,
        "model_name": "DeepSeek",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Gemma_3, EN, MH
    {
        "model": models.Gemma_3,
        "model_name": "Gemma_3",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # Gemma_3, ES, MH
    {
        "model": models.Gemma_3,
        "model_name": "Gemma_3",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Qwen_2_5, EN, MH
    {
        "model": models.Qwen_2_5,
        "model_name": "Qwen_2_5",
        "language": "EN",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_EN,
        "templates": prompts_HAPA.templates_EN
    },
    # Qwen_2_5, ES, MH
    {
        "model": models.Qwen_2_5,
        "model_name": "Qwen_2_5",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Salamandra, ES, MH
    {
        "model": models.Salamandra,
        "model_name": "Salamandra",
        "language": "ES",
        "health_type": "MH",
        "diagnoses": diagnoses.MH_diagnoses_ES,
        "templates": prompts_HAPA.templates_ES
    },
    # Salamandra, EN, MH
    {
        "model": models.Salamandra,
        "model_name": "Salamandra",
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