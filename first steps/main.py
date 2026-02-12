from transformers import pipeline # type: ignore
import config
import models
import experiments
import diagnoses
import prompts_HAPA

# Pipeline
filler = pipeline(
    "fill-mask",
    model = models.DisorBERT,
    device = config.device
)

# Experiments
#TODO