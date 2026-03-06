import experiments_matrix
import evaluators

experiments = experiments_matrix.experiments

for exp in experiments:

    print(f"{exp['model_name']}_{exp['language']}_{exp['health_type']}")

    # Evaluators
    results = evaluators.LLM_bias_per_diagnosis(
        model=exp["model"],
        diagnoses=exp["diagnoses"],
        templates=exp["templates"],
        language=exp["language"]
    )

    # Save
    results.to_csv(
        f"../results/{exp['model_name']}_{exp['language']}_{exp['health_type']}.csv",
        index=True,
        encoding='utf-8'
    )