from transformers import pipeline # type: ignore
import config
import models
import evaluators
import diagnoses
import prompts_HAPA
import vocabulary_utils
import tokens

# config
model = models.DisorBERT
device = config.device
male_tokens = tokens.male_EN
female_tokens = tokens.female_EN
proper_nouns_csv = "proper nouns/proper_nouns_EN.csv"
MH_diagnoses = diagnoses.MH_diagnoses_EN
non_MH_diagnoses = diagnoses.non_MH_diagnoses_EN
templates = prompts_HAPA.templates_EN

# Pipeline
filler = pipeline(
    "fill-mask",
    model = model,
    device = device
)

# Token vocabulary
male_vocabulary, female_vocabulary= vocabulary_utils.load_token_vocabularies(
    male_tokens = male_tokens,
    female_tokens = female_tokens,
    proper_nouns_csv = proper_nouns_csv
)

# Evaluators
MH_results = evaluators.RQ1_2210_15144v2(
    filler = filler,
    diagnoses = MH_diagnoses,
    templates = templates,
    female_vocabulary = female_vocabulary,
    male_vocabulary = male_vocabulary
)

non_MH_results = evaluators.RQ1_2210_15144v2(
    filler = filler,
    diagnoses = non_MH_diagnoses,
    templates = templates,
    female_vocabulary = female_vocabulary,
    male_vocabulary = male_vocabulary
)

MH_results.to_csv('results/MH_results.csv', index = True, encoding = 'utf-8')
non_MH_results.to_csv('results/non_MH_results.csv', index = True, encoding = 'utf-8')