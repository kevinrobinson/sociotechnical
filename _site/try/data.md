# Python functions for reviewing your data

- "tools to diagnose whether a given fairness issue might be addressed by collecting more training data from a particular subpopulation ... and to predict how much more data is needed"
- "support in identifying relevant subpopulations"
- "tools to help actively guide data collection / curation processes"


## Reviewing label categories
The choice of what categories labelers us significantly impacts the performance of ML systems built on that data, especially when the labeling is about human activity (see Hanna et al. 2020 for further citations).


## Reviewing upstream labeling procedures
The way examples are framed can influence labelers, which can be a source of validity concerns (eg, [Mallari et al. 2020](https://arxiv.org/pdf/2002.01111v1.pdf)).  This is especially true if labelers are chosen primarily based on cost, and they lack domain knowledge or have been sampled from a distribution different than the people whose lives will be impacted by the ML system.

Also look for information loss that comes from aggregation or quantization at labeling time.


## Sanity-checking the dataset


## Looking at errors
1. Review samples of errors
2. Look for patterns (eg, https://f38b40a4-5763-4ae2-9f1f-1f75572afbb5.filesusr.com/ugd/1acfaf_4b2b106eaf6a40a89185eccacf822ea1.pdf)


## Revising training datasets
Industry practitioners more often turn to the data first, and usually have control data collection or curation (Holstein et al. 2019).

1. Increasing training set size
2. Measuring additional variables



