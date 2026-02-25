from transformers import pipeline # type: ignore
import config
import evaluators
import vocabulary_utils
import BERT_matrix
import RoBERTa_matrix
import BETO_matrix

experiments = BERT_matrix.experiments + RoBERTa_matrix.experiments + BETO_matrix.experiments

for exp in experiments:

    print(f"{exp["model_name"]}_{exp["language"]}_{exp["health_type"]}")

    # Pipeline
    filler = pipeline(
        "fill-mask",
        model = exp["model"],
        device = config.device
    )

    # Token vocabulary
    male_vocabulary, female_vocabulary = vocabulary_utils.load_token_vocabularies(
        male_tokens = exp["male_tokens"],
        female_tokens = exp["female_tokens"],
        proper_nouns_csv = exp["proper_nouns_csv"]
    )

    # Evaluators
    results = evaluators.RQ1_2210_15144v2(
        filler = filler,
        diagnoses = exp["diagnoses"],
        templates = exp["templates"],
        female_vocabulary = female_vocabulary,
        male_vocabulary = male_vocabulary
    )

    # Results
    results.to_csv(
        f"../results/{exp['model_name']}_{exp['language']}_{exp['health_type']}.csv",
        index = True,
        encoding = 'utf-8'
    )