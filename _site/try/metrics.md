# Picking your first fairness metric
In some ways, choosing fairness metrics come with both all the existing challenges of choosing business or SLA metrics, but also with much harder sociotechnical challenges.

It can be helpful to think of these just like other software engineering tests - no unit test guarantees you are building great software, just like no type system guarntees you are shipping the right product.  Fairness metrics are only a small part of the work, but they can help teams in the same way that small tools like linters can.



## 1. Ensure test data has sufficient representation

## 2. Check that test data makes sense for deployment context
Before deploying, review whether the training data matches the deployment target as best you can.  If you are taking a dataset trained on Reddit posts and deploying it to analyze language for K12 student essays, you will probably run into problems.  But even subtle mismatches like differences between models trained on data from one time period, or on a sample of the deployment population can lead to issues.

> (this visualization)


## 3. Add observability and monitoring distribution drift
Like with all production deployments, adding observability is critical for gaining visibility into how production services are performing.  For fairness questions, some ways to get started are:
- monitor distribution of predictions over time
- check for out-of-distribution inputs

> "...we had a couple of deployments which regressed in serious ways which our error rate did not reflect..." ([Cramer et al. 2019])(https://algorithmicbiasinpractice.files.wordpress.com/2019/02/fat_2019tutorial_algorithmicbiasinpractice.pdf)

## 4. Invite input from diverse stakeholders on what fairness means
This is often one of the most efficient and practical steps a team can take, but may involve bringing in external collaborators or partners.

Some starting points for questions are:
- What happens if the system's predictions are wrong?
- What subset of people would be harmed the most by wrong predictions?

See Brown et al. (2020) for a narrative approach to these conversations, Young et al. (2019) for ways to get feedback on design documents, and Martin et al. (2020) for ways to involve stakeholders in more complex assumptions about feedback loops.

## 5. Choosing specific fairness metrics
Two helpful metrics to get started with are false positive rate or false negative rate.  Beyond those, you can also look at them for particular subgroups (eg, across all elements of subgroups).

## 6. Group fairness metrics
After you've set up for first fairness metrics, it may also make sense to look at group fairness metrics.  The most common are "demographic parity" and "equal opportunity," but tradeoffs in these choices often require more communication with stakeholders.  These are described in depth in *Equality of Opportunity in Supervised Learning* ([Hardt et al. 2016](https://arxiv.org/abs/1610.02413)) and can be explored interactively in *Attacking discrimination with smarter machine learning* [Wattenberg et al. 2016](https://research.google.com/bigpicture/attacking-discrimination-in-ml/).



In the way way that other metrics like code coverage are only a small part of understanding the quality of a codebase, fairness metrics  are only a small component of the fairness work on a project.
