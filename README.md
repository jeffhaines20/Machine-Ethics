# Machine-Ethics

Trained and compared LSTM, GRU, BERT, and DistilBERT models to predict human moral judgments on the ETHICS benchmark (Hendrycks et al., 2021). The dataset and its details are at https://github.com/hendrycks/ethics. The project also includes token-level model interpretability (via `transformers_interpret`) and a deployed Hugging Face demo.

## Results (per-example accuracy on the ETHICS test sets)

| Model | Deontology | Justice | Virtue | Commonsense |
| --- | --- | --- | --- | --- |
| Bi-Directional LSTM | 0.696 | 0.641 | 0.690 | 0.723 |
| GRU | 0.691 | 0.624 | 0.642 | 0.533 |
| BERT | 0.764 | 0.703 | 0.822 | 0.787 |
| DistilBERT | 0.771 | 0.735 | 0.804 | 0.780 |

As expected, the fine-tuned transformers (BERT and DistilBERT) clearly outperformed the from-scratch recurrent models (LSTM and GRU).

## Evaluation caveat (please read before comparing to the ETHICS paper)

These figures are **per-example binary accuracy** and are **not directly comparable** to the headline numbers reported in the ETHICS paper. An earlier version of this README compared them to the paper's best models and claimed to beat that leaderboard. That comparison was not valid, for three reasons, and it has been removed:

1. **Metric mismatch.** For the justice, deontology, and virtue tasks, the ETHICS paper reports a stricter grouped (exact-match) score, in which every related item in a group must be classified correctly for the group to count. Per-example accuracy is an easier target, so the numbers above should not be read as outperforming the paper's models. The clearest check is the commonsense morality task, which is scored the same way I scored mine: there my best model (about 0.78) is below the paper's best (about 0.90), as expected.
2. **Label imbalance on virtue.** Each virtue example contains five candidate statements with one correct, so roughly 80 percent of test rows are negative. A trivial "always predict negative" baseline already scores about 0.80, which is why per-example accuracy is not meaningful for this task and why the paper uses the grouped metric.
3. **Model-selection leakage.** The recurrent models used the test set as validation data for early stopping, so those test figures are optimistically biased. A clean setup would hold out a separate validation split and evaluate on the test set only once.

A faithful comparison to the paper would re-score justice, deontology, and virtue with the grouped exact-match metric and use a held-out validation split. I would expect the transformer results to remain respectable but to sit at or below the published numbers rather than above them.

## What this project demonstrates

- Fine-tuning and comparing multiple architectures (LSTM, GRU, BERT, DistilBERT) with `ktrain` and Hugging Face.
- Token-level model interpretability with `transformers_interpret`.
- Deployment of the best model to Hugging Face Spaces for interactive use: https://huggingface.co/spaces/jeffhaines/Ethical_Judgment_Generator

## Why machine ethics

Building models that can predict human moral judgments is useful in two respects. First, automated systems increasingly make decisions that affect people's lives, from self-driving cars to lending, hiring, and criminal sentencing. Some of these can be handled by hard-coded rules, but as automation grows, systems will meet cases where fixed rules do not apply or give clearly wrong answers. (A rule like "do not run a red light" is generally good but can be disastrous in rare situations.) In such cases, some capacity for moral reasoning becomes valuable.

Second, models like these may help study and improve human moral reasoning. The benchmark cases are meant to be ones with wide agreement, but people still disagree, and some of that disagreement comes from faulty reasoning. Common fallacies such as appeal to popularity, appeal to nature, and ad hominem appear in moral arguments as they do elsewhere, and tools that surface them could be useful.

## Repository contents

- `Commonsense_Ethics.ipynb`, `Deontology.ipynb`, `Justice.ipynb`, `Virtue_Ethics.ipynb`: training and evaluation for each task.
- `commonsense_ethics/`: saved DistilBERT model parameters and config.
- Data: the ETHICS benchmark (https://github.com/hendrycks/ethics), not redistributed here.
