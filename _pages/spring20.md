---
title: DataResponsibly - Course
layout: default_course
permalink: /spring20/
author: Julia Stoyanovich
---

# [DS-GA 3001.009: Special Topics in Data Science:<br> Responsible Data Science](.)

## New York University, Center for Data Science, Spring 2020


**Lecture:** Mondays from 11am-12:40pm; **Lab:** Mondays from 3:30pm-4:20pm

**Location:** 60 5th Avenue, Room 110

**Instructor:** [Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich), Assistant Professor of Data Science, Computer Science and Engineering.
<br>Office hours Mondays 1:30-3pm or by appointment, at 60 5th Avenue, Room 703.

**Section Leader:** [Brina Seidel](mailto:bs3743@nyu.edu). Office hours Thursdays 3:30-4:30pm or by appointment, at 60 5th Avenue, Room 660.

**Grader:** [Prasanthi Gurumurthy](mailto:pg1899@nyu.edu). Office hours Wednesdays, 10:30-11:30am or by appointment, at 60 5th Avenue, Room 665.

**Syllabus:** [pdf](https://dataresponsibly.github.io/courses/documents/spring20/RDS_Syllabus_2020.pdf)

**Course Description:**
    
The first wave of data science focused on accuracy and efficiency -- on what we _can_ do with data. The second wave focuses on responsibility -- on what we _should_ and _shouldn't_ do. Irresponsible use of data science can cause harm on an unprecedented scale. Algorithmic changes in search engines can sway elections and incite violence; irreproducible results can influence global economic policy; models based on biased data can legitimize and amplify racist policies in the criminal justice system; algorithmic hiring practices can silently and scalably violate equal opportunity laws, exposing companies to lawsuits and reinforcing the feedback loops that lead to lack of diversity.  Therefore, as we develop and deploy data science methods, we are compelled to think about the effects these methods have on individuals, population groups, and on society at large.

Responsible Data Science is a technical course that tackles the issues of ethics, legal compliance, data quality, algorithmic fairness and diversity, transparency of data and algorithms, privacy, and data protection. The course is developed and taught by [Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich), Assistant Professor at the Center for Data Science and at the Tandon School of Engineering, and member of the [NYC Automated Decision Systems Task Force](https://www1.nyc.gov/site/adstaskforce/index.page).

**Prerequisites:** Introduction to Data Science, Introduction to Computer Science, or similar courses.

**Lab Materials:** Labs will be conducted using [Jupyter Hub](https://dsga-3001009.rcnyu.org/). Students should use their NYU NetID to log in, and click the "Assignments" tab to find the material for each week. After lab, links to the notebook for each class will be included on this page.

## Background Reading (required)

*  Barocas and Selbst (2016) "Big Data’s Disparate Impact" [pdf](http://www.californialawreview.org/wp-content/uploads/2016/06/2Barocas-Selbst.pdf)
*  White House Report on Big Data (2014) "Big Data: Seizing Opportunities, Preserving Values" [pdf](https://obamawhitehouse.archives.gov/sites/default/files/docs/big_data_privacy_report_may_1_2014.pdf)
*  Brauneis and Goodman (2017) "Algorithmic Transparency for the Smart City" [pdf](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3012499)
*  Kroll et al. (2017) "Accountable Algorithms" [pdf](https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3/)

## Background Reading (optional)
   
*  Matthew Salganik "Bit by Bit: Social Research in the Digital Age" ([read online](https://www.bitbybitbook.com/en/1st-ed/preface/))
*  Cathy O’Neil "Weapons of Math Destruction"
*  Frank Pasquale "The Black Box Society"
*  Virginia Eubanks "Automating Inequality"

## Schedule

* See Spring 2019 schedule, slides, labs: [DS-GA 3001.009: Special Topics in Data Science: Responsible Data Science](https://dataresponsibly.github.io/courses/spring19)

This weekly schedule is tentative and is subject to change.

|Date         | Topic | Materials | Assignments |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|:--------------------|
| Jan&nbsp;27 | **Lecture:** Introduction and background.  Algorithmic fairness. <br> _Topics:_ Course outline, aspects of responsibility in data science through recent examples. Fairness in classification. The importance of a socio-technical perspective: stakeholders and trade-offs. <br> _Reading:_ <br> "Bias in Computer Systems", Friedman and Nissenbaum (1996) [ACM DL](https://dl.acm.org/citation.cfm?id=230561) <br> "Machine Bias", Angwin, Larson, Mattu, Kirchner (2016) [ProPublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) <br> "Data, Responsibly", Abiteboul and Stoyanovich (2015) [ACM SIGMOD blog](http://wp.sigmod.org/?p=1900) <br> “Fairness through awareness”, Dwork, Hardt, Pitassi, Reingold, Zemel (2012) [ACM DL](https://dl.acm.org/citation.cfm?doid=2090236.2090255) <br> "On the (im)possibility of fairness", Friedler, Scheidegger, Venkatasubramanian (2016) [arXiv](https://arxiv.org/abs/1609.07236)  | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture1.pdf) |  |
| Jan&nbsp;27 | **Lab:** Intro to Jupyter Hub, ProPublica's Machine Bias | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab_1_2020.ipynb) |  |
| Feb&nbsp;3  | **Lecture:** Algorithmic fairness continued. <br> _Topics:_ Fairness in risk assessment.  Fairness in ranking. <br> _Reading:_ <br>  "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments", Chouldechova (2017) [arXiv](https://arxiv.org/abs/1703.00056) <br> "Inherent Trade-Offs in the Fair Determination of Risk Scores", J. Kleinberg, S. Mullainathan, M. Raghavan (2017) [pdf](http://drops.dagstuhl.de/opus/volltexte/2017/8156/pdf/LIPIcs-ITCS-2017-43.pdf) <br> "Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions", Mitchell, Porash, Barocas (2018) [arXiv](https://arxiv.org/abs/1811.07867) <br> "Dissecting racial bias in an algorithm used to manage the health of populations", Obermeyer, Powers, Vogel, Mullainathan(2019) [Science](https://science.sciencemag.org/content/366/6464/447) |  [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture2.pdf) |  |
| Feb&nbsp;3  |**Lab:** IBM's AI Fairness 360 toolkit <br> _Reading:_ <br> "AI Fairness 360: An Extensible Toolkit for Detecting, Understanding, and Mitigating Unwanted Algorithmic Bias", R. Bellamy et al. (2018) [pdf](https://arxiv.org/pdf/1810.01943.pdf) <br> "Data preprocessing techniques for classification without discrimination", F. Kamiran and T. Calders (2012) [pdf](https://link.springer.com/content/pdf/10.1007%2Fs10115-011-0463-8.pdf) <br> "Certifying and removing disparate impact", M. Feldman, S. A. Friedler, J. Moeller, C. Scheidegger, and S. Venkatasubramanian (2015) [pdf](https://arxiv.org/pdf/1412.3756.pdf) | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab_2_2020.ipynb)  |  |
| Feb&nbsp;10 | **Lecture:** Data cleaning <br> _Topics:_  Overview of data cleaning <br>_Reading:_<br>"Profiling relational data: a survey", Abedjan, Golab, Naumann (2015) [pdf](https://dataresponsibly.github.io/courses/documents/Abedjan_2015.pdf)<br> "Quantitative data cleaning for large databases", Hellerstein (2008) [pdf](https://dataresponsibly.github.io/courses/documents/Hellerstein_2008.pdf)   | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture3.pdf)|  |  |
| Feb&nbsp;10 | **Lab:** IBM's AI Fairness 360 toolkit <br> _Reading:_ <br> "FairPrep: Promoting Data to a First-Class Citizen in Studies on Fairness-Enhancing Interventions", S. Schelter, Y. He, J. Khilnani, and J. Stoyanovich (2019) [pdf](https://arxiv.org/pdf/1911.12587.pdf)  | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab_3_2020.ipynb) | HW1 assigned |
| Feb&nbsp;17 | No class, university holiday |  |  |
| Feb&nbsp;24  | **Lecture (part 1):**  Fairness and causality<br> _Topics:_ Counterfactual fairness<br>"The long road to fairer algorithms", M. Kushner, J. Loftus (2020) [Nature](https://www.nature.com/articles/d41586-020-00274-3) <br>"Counterfactual fairness", M. Kusner, J. Loftus, C. Russell, R. Silva(2017) [pdf](https://papers.nips.cc/paper/6995-counterfactual-fairness.pdf) <br> **Lecture (part 2):** Data profiling<br> _Topics:_ Types of data profiling tasks, overview of the relational model | [slides(1)](https://dataresponsibly.github.io/courses/documents/spring20/Lecture4.pdf) [slides(2)](https://dataresponsibly.github.io/courses/documents/spring20/Lecture5.pdf) |  HW1 due<br> |
| Feb&nbsp;24   | **Lab:** Data profiling and data cleaning<br> course project discussion  | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab_4_2020.ipynb) | project assigned |
| Mar&nbsp;2| **Lecture (part 1):**  Data profiling continued<br> _Topics:_ Discovering uniques, frequent itemset and association rule mining<br> **Lecture (part 2):** Anonymity and privacy <br> _Topics:_ Overview of responsible data sharing. Anonymization techniques; the limits of anonymization. Harms beyond re-identification.<br> _Reading:_ <br>"The Belmont Report" (1979) [pdf](https://www.hhs.gov/ohrp/sites/default/files/the-belmont-report-508c_FINAL.pdf) <br> "Critical questions for Big Data", danah boyd and Kate Crawford (2012) [pdf](https://www.tandfonline.com/doi/pdf/10.1080/1369118X.2012.678878) | [slides(1)](https://dataresponsibly.github.io/courses/documents/spring20/Lecture5.pdf) [slides(2)](https://dataresponsibly.github.io/courses/documents/spring20/Lecture6.pdf)|  |
| Mar&nbsp;2 | **Lab:** Data profiling and data cleaning | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab_4_2020.ipynb)| |
| Mar&nbsp;9 | **Lecture:** Anonymity and privacy <br> _Topics:_ Differential privacy; privacy-preserving synthetic data generation; exploring the privacy / utility trade-off. <br> _Reading:_ <br>"A firm foundation for private data analysis", C. Dwork (2011) [ACM DL](https://dl.acm.org/citation.cfm?doid=1866739.1866758)<br>"Can a set of equations keep U.S. census data private?", J. Mervis (2019) [Science](https://www.sciencemag.org/news/2019/01/can-set-equations-keep-us-census-data-private)  | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture6.pdf) |  project proposal due|
| Mar&nbsp;9 | **Lab:** Data Synthesizer<br> _Reading:_ <br>"DataSynthesizer: Privacy-Preserving Synthetic Datasets", Ping, Stoyanovich, Howe (2017) [ACM DL](https://dl.acm.org/citation.cfm?doid=3085504.3091117)  | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab6_2020.ipynb)| HW2 assigned |
| Mar&nbsp;16 | No class, university holiday |  |  |
| Mar&nbsp;23  | **Lecture:** Ethical frameworks<br> _Reading:_ "The Belmont Report" (1979) [pdf](https://www.hhs.gov/ohrp/sites/default/files/the-belmont-report-508c_FINAL.pdf)<br> "The Menlo Report" (2012) [pdf](http://www.caida.org/publications/papers/2012/menlo_report_actual_formatted/menlo_report_actual_formatted.pdf) <br>"Chapter 6: Ethics. Bit by Bit: Social Research in the Digital Age", Matthew Salganik (2017) [online](https://www.bitbybitbook.com/en/1st-ed/ethics/)  | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture7.pdf) |  |
| Mar&nbsp;23 | **Lab:**  Ethical frameworks |  |  |
| Mar&nbsp;30  | **Lecture:** Transparency <br> _Topics:_ Auditing black-box models; explainable machine learning.<br>_Reading:_<br>"Why should I trust you? Explaining the predictions of any classifier", Ribeiro, Singh, Guestrin (2016) [pdf](https://dl.acm.org/citation.cfm?doid=2939672.2939778)<br>"Algorithmic transparency via quantiative input influence: theory and experiments with learning systems", Datta, Sen, Zick (2016) [pdf](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7546525)<br>"A unified approach to interpreting model predictions", Lundberg and Lee (2017) [pdf](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf) | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture8.pdf) |  HW2 due |
| Mar&nbsp;30 | **Lab:** LIME | [notebook](https://github.com/DataResponsibly/courses/blob/master/documents/spring20/RDS_Lab8_2020.ipynb) |  |
| Apr&nbsp;6  | **Lecture:** Transparency <br> _Topics:_ Discrimination in online ad delivery. <br>_Reading:_<br>"Automated Experiments on Ad Privacy Settings", Datta, Tschantz, Datta (2015) [pdf](https://content.sciendo.com/view/journals/popets/2015/1/article-p92.xml) <br>"Discrimination through optimization: How Facebook’s ad delivery can lead to skewed outcomes", Ali, Sapiezynski, Bogen, Korolova, Mislove, Rieke (2019) [pdf](https://arxiv.org/pdf/1904.02095.pdf) <br> "Facebook has been charged with housing discrimination by the US government", Russell Brandom for The Verge, Mar 28, 2019 [read online](https://www.theverge.com/2019/3/28/18285178/facebook-hud-lawsuit-fair-housing-discrimination) | [slides](https://dataresponsibly.github.io/courses/documents/spring20/Lecture9.pdf) |  HW3 assigned<p> project report draft due (**extended to Apr&nbsp;8**) |
| Apr&nbsp;6  | **Lab:** Transparency |  |  |
| Apr&nbsp;13  |**Lecture:** Interpretability <br> _Topics:_ TBD <br> _Reading:_ TBD |  | |
| Apr&nbsp;13 | **Lab:** Interpretability | |  |
| Apr&nbsp;20 | **Lecture:** RDS in practice: Guest lecture by [Robert Cheetham](https://www.azavea.com/about/teammate/robert-cheetham/), President and CEO of Azavea  <br> _Topics:_ Selecting your  <br> _Reading:_ TBD  |  | HW3 due|
| Apr&nbsp;20 | **Lab:** Final exam review |  |  |
| Apr&nbsp;27 | **Lecture:** Legal and regulatory frameworks <br> _Topics:_ Data protection, algorithmic impact assessment, regulating Automated Decision Systems (ADS) and AI <br> _Reading:_ TBD |  |  Final exam assigned (take-home) |
| Apr&nbsp;27 | **Lab:** Course project |  |  |
| May&nbsp;4 | **Lecture:** TBD <br> _Topics:_ TBD <br> _Reading:_ TBD |  | |
| May&nbsp;4  | **Lab:** TBD | |  |
| May&nbsp;11 | **Lecture:** Project presentations |  | project report due |
| May&nbsp;11  | **Lab:** Project presentations |  |  |
