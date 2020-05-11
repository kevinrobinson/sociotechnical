# Housing in Boston and ML fairness

I was exploring some visualizations and tools for ML fairness.  There's a lot of tools that focus narrowly of fairness metrics, but few that support people in considering the social and historical context where ML models are developed and deployed.

If you work on an interdisciplinary team, and collaborate directly with users impacted by the ML system you are making, you don't need to do this.  But few teams actually work like this, so often practicing ML engineers, data scientists and software engineers fill in that gap.

So I'm interested in embracing the more challenging UX, visualization and tooling work, and wanted to find a scenario and dataset that could be a test case for exploring new ideas.

In the process, I ran into the Boston Housing Dataset, and here's my story.

## Discovering the dataset

## Looking at the data

## Methodology
There's some work published on the Boston housing data set that might be of interest, and doesn't seem like it's come up in this issue.  Here's a reference to the original [Harrison and Rubinfeld (1976)](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/22636/0000186.pdf?sequence=1&isAllowed=y) paper, which used the dataset to make estimates about pricing of air quality.

A few years after that, the dataset was used in *4.4 Robust Estimation of a Hedonic Housing-Price Equation* in the [Belsey et al. textbook (1980)](https://onlinelibrary.wiley.com/doi/book/10.1002/0471725153).  I can't access this source so I'm not sure what's actually in there, but my assumption is that might have been the first place the dataset was used as an example of estimating the median value of owner-occupied houses within a census tract.  I'm not sure where this model was supposed to  be deployed, or where it was supposed to generalize to :)

In the 1990s, other papers discussed methodological issues encoded in the dataset, including *On the Harrison and Rubinfeld Data* ([Gilley and Pace 2016](https://www.sciencedirect.com/science/article/abs/pii/S0095069696900522?via%3Dihub)) and *Using the Spatial Configuration of the Data to Improve Estimation* ([Pace and Gilley 2017](https://link.springer.com/article/10.1023/A:1007762613901)).

In the 2010s, another author wrote about another set of methodological issues, including *Revisiting the Boston data set - Changing the units of observation affects estimated willingness to pay for clean air* ([Bivand 2017](https://openjournals.wu.ac.at/ojs/index.php/region/article/view/107)) and *Revisiting the Boston Data Set: A Case Study in the Challenges of System Articulation* ([Bivand 2015](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2719454)).  The latter explicitly discusses challenges in how to: *"alert 'new arrivals' to existing bodies of knowledge that can inform the ways in which they structure their work... a particular matter of opportunity and concern that most of the data used is secondary."*

More recently, this medium post ([Carisle 2019](https://medium.com/@docintangible/racist-data-destruction-113e3eff54a8)) talks about the transformation of the "B" column, both as a technical issue and what else it might imply.

## scikit-learn discussion

## Ames dataset
If you're curious about the Ames dataset, one key difference is that rows are individual home listings rather than aggregated values for entire census tracts.  The author has written that it was developed for an undergraduate course in 2010 because inflation made its housing prices seem unrealistic to students in 2010 ([DeCock 2011](http://jse.amstat.org/v19n3/decock.pdf)).  The dataset is taken from a college town in Iowa that is more [homogenous](https://en.wikipedia.org/wiki/Ames,_Iowa) than most parts of the country.  I haven't read anything on where people would expect to deploy a model trained on this dataset, and where it would be expected to generalize to.

In the city's [2019 Analysis of Impediments to Fair Housing Choice](https://www.cityofames.org/home/showdocument?id=51543), they state that "most of the respondents were of white/European- American descent."  It also states that "housing discrimination is not a major issue in Ames as perceived by both housing consumers and housing producers/providers," and goes on to say:

> Housing discrimination is not a major issue in Ames. However, there were still 7% of the general housing renters who felt it was, 6% of the subsidized housing renters, 4 of the ISU students and 2% by homeowner also found housing discrimination an issue.

Importantly, the majority of housing units in Ames are not owner-occupied ("57% are renter-occupied") and cost burden is a signficant problem for renders ("42% of the renters had a cost burden of >50% [of their income spent on rent]").

I'm sure folks much more thoughtful than me can make other analyses here; my point is just that for folks modeling housing prices and asking questions of fairness, these might be useful data points that are publicly available.

## Diabetes dataset

## Beyond fairness as a technical question
That being said, none of these really consider fairness questions broadly (eg, [Selbst et al. (2015)](https://andrewselbst.files.wordpress.com/2019/10/selbst-et-al-fairness-and-abstraction-in-sociotechnical-systems.pdf)).  The particular historical and social context of the Boston area in the 1970s is very much not a neutral example :)  At the national level there was [legislation on housing discrimination](https://en.wikipedia.org/wiki/Civil_Rights_Act_of_1968#Title_VIII%E2%80%93IX:_Fair_Housing_Act) passed a few years earlier (note that in practice this has been [mostly unenforced to this day](https://www.gao.gov/products/GAO-10-905)).  At the local level, [legal challenges](https://www.cityofboston.gov/Images_Documents/Guide%20to%20the%20BHA%20Reports%20and%20publications%20relat_tcm3-25949.pdf) to the Boston Housing Authority led to a consent decree and the institution being placed in receivership.  Of course in the years before the 1970s other issues related to fairness in housing were widespread, including [redlining](https://www.bostonfairhousing.org/timeline/1934-1968-FHA-Redlining.html) and [land use regulations](https://www.bostonfairhousing.org/timeline/1970s-present-Local-Land_use-Regulations.html).

Relatedly, the [Morgan v. Hennigan case](https://www.cityofboston.gov/images_documents/Guide%20to%20the%20Law%20Department%20records%20Morgan%20v.%20Hennigan%20and%20related%20cases%20fil_tcm3-50853.pdf) happened in federal court during that same time period, after conflicts between the state Board of Education, the Boston City Council, and other groups.  This led to a federal court order to desegrate schools, which involved protests and violence, all reported as national news at the time.  Here's a [retrospective](https://www.wbur.org/news/2014/09/05/boston-busing-anniversary) from a Boston news organization a few years ago, looking back at how some people experienced that time.

It's also important to know that housing discrimination is still very much an [issue today](https://www.bostonfairhousing.org/timeline/1968-Housing-Discrimination-Today.html).  Here's a [HUD report from 2012](https://www.racialequitytools.org/resourcefiles/HUD-514_HDS2012.pdf), which of course is contested as well.  In the city that I live in within near Boston, it is still common to do "audit studies" on housing discrimination; here's the form from last year to [train to become an auditor](https://www.somervillema.gov/sites/default/files/Housing%20Discrimination%20Tester%20Training%2005.08.19[4].pdf).  In the city I live in, a [2017 survey](https://www.somervillema.gov/sites/default/files/affh-community-engagement-results.pdf) found that ~65% of residents surveyed reported experienced housing discrimination.  In 2019, the federal agency that oversees enforcement of the Fair Housing Act proposed a [new rule](https://www.federalregister.gov/documents/2019/08/19/2019-17542/huds-implementation-of-the-fair-housing-acts-disparate-impact-standard#sectno-citation-%E2%80%89100.7), which has not yet been adopted.  Different advocacy organizations have engaged with this in different ways (eg, [ACLU report](https://www.aclu.org/letter/aclu-comment-huds-proposed-rule-affirmatively-limiting-furthering-fair-housing), [Brookings post](https://www.brookings.edu/blog/techtank/2020/04/16/why-a-proposed-hud-rule-could-worsen-algorithm-driven-housing-discrimination/)).


### In closing
All this is to say, there are many aspects of fairness and there's a range of ways scikit-learn can choose to engage with those, and a range of choices it can make regarding what the project sees as its scope of professional responsibility.  These choices go far beyond just choosing the columns in a dataset, and I imagine different people will have different ideas about these questions :)

I'm excited there are folks in `scikit-learn` encouraging developers, data scientists, and researchers to ask questions about the wider sociotechnical context where their work exists, in the spirit of [Selbst et al. (2015)](https://andrewselbst.files.wordpress.com/2019/10/selbst-et-al-fairness-and-abstraction-in-sociotechnical-systems.pdf).  I hope this helps other folks curious about this particular dataset explore their questions a bit further, and will leave people to choose their own directions forward :)





