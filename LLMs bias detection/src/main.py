import experiments_matrix
import evaluators
import judge

experiments = experiments_matrix.experiments

for exp in experiments:

    print(f"{exp['model_name']}_{exp['language']}_{exp['health_type']}")

    # Evaluators
    results = evaluators.LLM_bias_per_diagnosis(
        model=exp["model"],
        diagnoses=exp["diagnoses"],
        templates=exp["templates"],
    )

    # Save
    filepath = f"../results/{exp['model_name']}_{exp['language']}_{exp['health_type']}.csv"
    results.to_csv(
        filepath,
        index=False,
        encoding='utf-8'
    )

    # Judge
    judge.evaluate_and_clean_csv(filepath, filepath)