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
    }
]