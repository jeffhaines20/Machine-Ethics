# Machine-Ethics
Uses GRUs, BERT, LSTMs, and distilbert to predict human moral judgments. More details abut the datasets and can be found at https://github.com/hendrycks/ethics. That repository also contains a leader board. Below I compare how my own models did compared to the best performing model on the leadersboards (best forming model for each dataset in bold):


 | Model | Deontology | Justice | Virtue Ethics | Commonsense |
| --- | --- | --- | --- | --- |
| Bi-Directional LSTM | 0.696 | 0.641 | 0.69 | 0.723 |
| GRU | 0.691 | 0.624 | 0.642 | 0.533 |
| BERT | 0.764 | 0.703 | **0.822** | 0.787 |
| distilbert | **0.771** | **0.735** | 0.804 | 0.78 |
| Leaderboard | 0.641 | 0.599 | 0.641 | **0.904** |

We can see that BERT and distilbert had the best accuracy of any of my models, and generally outperformed the leaderboard's top model, except on the commonsense dataset. 

Building neural networks that can reliably predict (and therefor make) moral judgments is useful in at least two respects: first it may allow for improved decision-making processes by machines. Already neural networks and other forms of artificial intelligence make decisions that can dramatically affect people's lives - self-driving cars, decisions about loans, hiring, and criminal justice sentencing are just some examples where automated decision making may dramatically impact a person's life. Although some decisions in those realms may be adequately handled by hardcoding moral rules into the systems, it is likely that, as automation progresses, machines will be faced with more cases where hardcoded rules either fail to apply to arrive at clearly wrong conclusions (e.g., for a simple example, "do not run a redlight" might be one hardcoded rule which is generally good but could lead to disaster in rare circumstances. In such situations, machines might need to be able to apply some moral reasoning for themselves. 

The second area where improving automated reasoning may be useful is in improving human moral reasoning. Although the cases in the datasets are supposed to all be cases where there is widespread or universal agreement on right behavior, sometimes people disagree and sometimes this disagreement is due to mistaken reasoning. Just as there can be errors of reasoning in other areas, there can be errors in moral reasoning. Many common logical fallacies, for example, such as appeal to popularity, appeal to nature, and ad hominems routinely appear in moral moral reasoning. There is no reason to think that artificial intelligence cannot improve on human reasoning there, as it has in other areas.
