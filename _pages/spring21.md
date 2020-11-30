---
title: DataResponsibly - Course
layout: default_course
permalink:
author: Julia Stoyanovich, George Wood
---

# [DS-UA 202 and DS-GA 1017: Responsible Data Science](.)

## New York University, Center for Data Science, Spring 2021

**Lecture A (DS-GA 1017):** Mondays 9:15am-10:55am<br>
**Lecture B (DS-UA 202):** Tuesdays 9:30am-12pm

**Lab A (DS-GA 1017):** Mondays 11:35am-12:25pm (blended)<br>
**Lab B (DS-GA 1017):** Wednesdays 9:30am-10:20am (online)<br>
**Lab C (DS-UA 202):** Wednesdays  9:30am-10:20am (online)<br>
**Lab D (DS-UA 202):** Wednesdays  10:25am-11:15am (blended)

**Instructors:**

[Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich), Assistant Professor of Data Science, Computer Science and Engineering<br>
[George Wood](https://gwood.me), Moore-Sloan Faculty Fellow, Center for Data Science

**Section Leaders:**

[Apurva Bhargava](mailto:ab8687@nyu.edu), DS-UA 202, office hours TBD<br>
[Jeewon Ha](mailto:jh6926@nyu.edu), DS-UA 202, office hours TBD<br>
[Prasanthi Gurumurthy](mailto:pg1899@nyu.edu), DS-GA 1017, office hours TBD<br>

**Graders:**

[Evaristus Ezekwem](mailto:evaristus.ezekwem@nyu.edu), DS-GA 1017, office hours TBD<br>
[Nan Wu](nw1045@nyu.edu), DS-GA 1017, office hours TBD

**Syllabi:**

[DS-UA 202](#)<br>
[DS-GA 1017](#)

**Course Description:**

The first wave of data science focused on accuracy and efficiency -- on what we _can_ do with data. The second wave focuses on responsibility -- on what we _should_ and _shouldn't_ do. Irresponsible use of data science can cause harm on an unprecedented scale. Algorithmic changes in search engines can sway elections and incite violence; irreproducible results can influence global economic policy; models based on biased data can legitimize and amplify racist policies in the criminal justice system; algorithmic hiring practices can silently and scalably violate equal opportunity laws, exposing companies to lawsuits and reinforcing the feedback loops that lead to lack of diversity.  Therefore, as we develop and deploy data science methods, we are compelled to think about the effects these methods have on individuals, population groups, and on society at large.

Responsible Data Science is a technical course that tackles the issues of ethics, legal compliance, data quality, algorithmic fairness and diversity, transparency of data and algorithms, privacy, and data protection. The course is developed and taught by [Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich) (Assistant Professor at the Center for Data Science and at the Tandon School of Engineering, and member of the [NYC Automated Decision Systems Task Force](https://www1.nyc.gov/site/adstaskforce/index.page)) and [George Wood](https://gwood.me) (Moore-Sloan Faculty Fellow at the Center for Data Science).

**Prerequisites:** Introduction to Data Science, Introduction to Computer Science, or similar courses.  

**Lab Materials:** Labs will be conducted using [Jupyter Hub](https://dsga-3001009.rcnyu.org/). Students should use their NYU NetID to log in, and click the "Assignments" tab to find the material for each week. After lab, links to the notebook for each class will be included on this page.

### Background Reading (required)

*  Barocas and Selbst (2016) "Big Data’s Disparate Impact" [pdf](http://www.californialawreview.org/wp-content/uploads/2016/06/2Barocas-Selbst.pdf)
*  White House Report on Big Data (2014) "Big Data: Seizing Opportunities, Preserving Values" [pdf](https://obamawhitehouse.archives.gov/sites/default/files/docs/big_data_privacy_report_may_1_2014.pdf)
*  Brauneis and Goodman (2017) "Algorithmic Transparency for the Smart City" [pdf](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3012499)
*  Kroll et al. (2017) "Accountable Algorithms" [pdf](https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3/)

### Background Reading (optional)

*  Matthew Salganik "Bit by Bit: Social Research in the Digital Age" ([read online](https://www.bitbybitbook.com/en/1st-ed/preface/))
*  Cathy O’Neil "Weapons of Math Destruction"
*  Frank Pasquale "The Black Box Society"
*  Virginia Eubanks "Automating Inequality"

## Schedule

This weekly schedule is tentative and is subject to change.

#### Week 1, Feb 1-5

**Lecture:** Introduction and background; Algorithmic fairness

*  Topics: Course outline, aspects of responsibility in data science through recent examples. Fairness in classification. The importance of a socio-technical perspective: stakeholders and trade-offs.
*  Reading:

   "Bias in Computer Systems", Friedman and Nissenbaum (1996) [ACM DL](https://dl.acm.org/citation.cfm?id=230561)  
   "Machine Bias", Angwin, Larson, Mattu, Kirchner (2016) [ProPublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)  
   "Mirror, Mirror", Arif Khan and Stoyanovich (2020) [Vol 1](https://dataresponsibly.github.io/comics/)  
   “Fairness through awareness”, Dwork, Hardt, Pitassi, Reingold, Zemel (2012) [ACM DL](https://dl.acm.org/citation.cfm?doid=2090236.2090255)  
   "On the (im)possibility of fairness", Friedler, Scheidegger, Venkatasubramanian (2016) [arXiv](https://arxiv.org/abs/1609.07236)  

**Lab:** Intro to Jupyter Hub; ProPublica's Machine Bias


#### Week 2, Feb 8-12

**Lecture:** Algorithmic fairness continued

*  Topics: Fairness in risk assessment. Fairness in ranking.
*  Reading:

   "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments", Chouldechova (2017) [arXiv](https://arxiv.org/abs/1703.00056)     
   "Inherent Trade-Offs in the Fair Determination of Risk Scores", J. Kleinberg, S. Mullainathan, M. Raghavan (2017) [pdf](http://drops.dagstuhl.de/opus/volltexte/2017/8156/pdf/LIPIcs-ITCS-2017-43.pdf)  
   "Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions", Mitchell, Porash, Barocas (2018) [arXiv](https://arxiv.org/abs/1811.07867)  
   "Dissecting racial bias in an algorithm used to manage the health of populations", Obermeyer, Powers, Vogel, Mullainathan (2019) [Science](https://science.sciencemag.org/content/366/6464/447)

**Lab:** IBM's AI Fairness 360 toolkit

#### Week 3, Feb 15-19

**Lecture:** Data cleaning

*  Topics: Overview of data cleaning
*  Reading:

   "Profiling relational data: a survey", Abedjan, Golab, Naumann (2015) [pdf](https://dataresponsibly.github.io/courses/documents/Abedjan_2015.pdf)  
   "Quantitative data cleaning for large databases", Hellerstein (2008) [pdf](https://dataresponsibly.github.io/courses/documents/Hellerstein_2008.pdf)    

**Lab:** IBM's AI Fairness 360 toolkit

#### Week 4, Feb 22-26

**Lecture:** Part 1: Fairness and causality; Part 2: Data profiling

*  Topics: Counterfactual fairness, types of data profiling tasks, overview of the relational model
*  Reading:

   "The long road to fairer algorithms", M. Kushner, J. Loftus (2020) [Nature](https://www.nature.com/articles/d41586-020-00274-3)  
   "Counterfactual fairness", M. Kusner, J. Loftus, C. Russell, R. Silva(2017) [pdf](https://papers.nips.cc/paper/6995-counterfactual-fairness.pdf)

**Lab:** Data profiling and data cleaning; course project discussion

#### Week 5, Mar 1-5

**Lecture:** Part 1: Data profiling continued; Part 2: Anonymity and privacy

*  Topics: Discovering uniques, frequent itemset and association rule mining; Overview of responsible data sharing. Anonymization techniques; the limits of anonymization. Harms beyond re-identification
*  Reading:

   "The Belmont Report" (1979) [pdf](https://www.hhs.gov/ohrp/sites/default/files/the-belmont-report-508c_FINAL.pdf)  
   "Critical questions for Big Data", danah boyd and Kate Crawford (2012) [pdf](https://www.tandfonline.com/doi/pdf/10.1080/1369118X.2012.678878)                                 

**Lab:** Data profiling and data cleaning

#### Week 6, Mar 8-12

**Lecture:** Anonymity and privacy continued

*  Topics: Differential privacy; privacy-preserving synthetic data generation; exploring the privacy / utility trade-off. 
*  Reading: 

   "A firm foundation for private data analysis", C. Dwork (2011) [ACM DL](https://dl.acm.org/citation.cfm?doid=1866739.1866758)  
   "Can a set of equations keep U.S. census data private?", J. Mervis (2019) [Science](https://www.sciencemag.org/news/2019/01/can-set-equations-keep-us-census-data-private)      

**Lab:** Data Synthesizer

#### Week 7, Mar 15-19

**Lecture:** Ethical frameworks

*  Reading: 

   "The Belmont Report" (1979) [pdf](https://www.hhs.gov/ohrp/sites/default/files/the-belmont-report-508c_FINAL.pdf)  
   "The Menlo Report" (2012) [pdf](http://www.caida.org/publications/papers/2012/menlo_report_actual_formatted/menlo_report_actual_formatted.pdf)  
   "Chapter 6: Ethics. Bit by Bit: Social Research in the Digital Age", Matthew Salganik (2017) [online](https://www.bitbybitbook.com/en/1st-ed/ethics/)

**Lab:** Ethical frameworks

#### Week 8, Mar 22-26

**Lecture:** Transparency I

*  Topics: Auditing black-box models; explainable machine learning
*  Reading:

   "Why should I trust you? Explaining the predictions of any classifier", Ribeiro, Singh, Guestrin (2016) [pdf](https://dl.acm.org/citation.cfm?doid=2939672.2939778)  
   "Algorithmic transparency via quantiative input influence: theory and experiments with learning systems", Datta, Sen, Zick (2016) [pdf](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7546525)  
   "A unified approach to interpreting model predictions", Lundberg and Lee (2017) [pdf](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf)  

**Lab:** LIME

#### Week 9, Mar 29-Apr 2

**Lecture:** Transparency II

*  Topics: Discrimination in online ad delivery
*  Reading: 

   "Automated Experiments on Ad Privacy Settings", Datta, Tschantz, Datta (2015) [pdf](https://content.sciendo.com/view/journals/popets/2015/1/article-p92.xml)      

**Lab:** SHAP

#### Week 10, Apr 5-9

**Lecture:** Transparency III

*  Topics: Discrimination in online ad delivery, continued
*  Reading:

   "Discrimination through optimization: How Facebook’s ad delivery can lead to skewed outcomes", Ali, Sapiezynski, Bogen, Korolova, Mislove, Rieke (2019) [pdf](https://arxiv.org/pdf/1904.02095.pdf)  
   "Facebook has been charged with housing discrimination by the US government", Russell Brandom for The Verge, Mar 28, 2019 [read online](https://www.theverge.com/2019/3/28/18285178/facebook-hud-lawsuit-fair-housing-discrimination) 

**Lab:** Course project discussion; working through an example of an ADS

#### Week 11, Apr 12-16

**Lecture:** RDS in practice: Guest lecture

**Lab:** Final exam review

#### Week 12, Apr 19-23

**Lecture:** Interpretability

*  Topics: What is interpretability? 
*  Reading:

   "The Intuitive Appeal of Explainable Machines",  A. Selbst and  S. Barocas (2018) [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3126971)  
   "Nutritional Labels for Data and Models", J. Stoyanovich and B. Howe (2019) [pdf](http://sites.computer.org/debull/A19sept/p13.pdf)  
   "The Imperative of Interpretable Machines",  J. Stoyanovich,  J. Van Bavel,  T. West (2020) [link](https://rdcu.be/b3xJe)      

**Lab:** Course project discussion; working through an example of an ADS

#### Week 13, Apr 26-30

**Lecture:** Legal and regulatory frameworks

*  Topics: Data protection, algorithmic impact assessment, regulating Automated Decision Systems (ADS) and AI 
*  Reading:

   GDPR [link](https://gdpr-info.eu)  
   Canadian Directive on Automated Decision-Making [link](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=32592)  
   NYC ADS Task Force Report [pdf](https://www1.nyc.gov/assets/adstaskforce/downloads/pdf/ADS-Report-11192019.pdf)
   "Disparate Impact in Big Data Policing",  A. Selbst (2017)   [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2819182)  
   "Ensuring a Future that Advances Equity in Algoritmic Employment Decisions",  J. Yang (2019) [pdf](https://www.urban.org/sites/default/files/publication/101676/testimony_future_of_work_and_technology_-_jenny_yang_0_1.pdf)

**Lab:** Slack; course project discussion

#### Week 14, May 3-7

**Lecture:** Project presentations

**Lab:** Project presentations
