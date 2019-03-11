---
title: DataResponsibly - Course
layout: default
permalink: /spring19/
author: Julia Stoyanovich
redirect_from: "/"
---

# [DS-GA 3001.009: Special Topics in Data Science:<br> Responsible Data Science](.)

## New York University, Center for Data Science, Spring 2019


**Lecture:** Mondays from 11am-12:40pm; **Lab:** Thursdays from 5:20pm-6:10pm

**Location:** 60 5th Avenue, Room 110

**Instructor:** [Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich), Assistant Professor of Data Science, Computer Science and Engineering.
<br>Office hours Mondays 1:30-3pm or by appointment, at 60 5th Avenue, Room 605.

**Section Leader:** [Udita Gupta](mailto:ung200@nyu.edu). Office hours Thursdays 4-5pm at 60 5th Avenue, Room 663.

**Syllabus:** [pdf](https://dataresponsibly.github.io/courses/documents/spring19/Syllabus_DS-GA-3001.009_SP_2019.pdf)

**Course Description:**
    
The first wave of data science focused on accuracy and efficiency -- on what we _can_ do with data. The second wave focuses on responsibility -- on what we _should_ and _shouldn't_ do. Irresponsible use of data science can cause harm on an unprecedented scale. Algorithmic changes in search engines can sway elections and incite violence; irreproducible results can influence global economic policy; models based on biased data can legitimize and amplify racist policies in the criminal justice system; algorithmic hiring practices can silently and scalably violate equal opportunity laws, exposing companies to lawsuits and reinforcing the feedback loops that lead to lack of diversity.  Therefore, as we develop and deploy data science methods, we are compelled to think about the effects these methods have on individuals, population groups, and on society at large.

Responsible Data Science is a technical course that tackles the issues of ethics, legal compliance, data quality, algorithmic fairness and diversity, transparency of data and algorithms, privacy, and data protection. The course is developed and taught by [Julia Stoyanovich](https://engineering.nyu.edu/faculty/julia-stoyanovich), Assistant Professor at the Center for Data Science and at the Tandon School of Engineering, and member of the [NYC Automated Decision Systems Task Force](https://www1.nyc.gov/office-of-the-mayornews/251-18/mayor-de-blasio-first-in-nation-task-force-examine-automated-decision-systems-used-by).

**Prerequisites:** Introduction to Data Science, Introduction to Computer Science, or similar courses.

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

This weekly schedule is tentative and is subject to change.

|Date         | Topic | Materials | Assignments |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|:--------------------|
| Jan&nbsp;28 | **Lecture:** Introduction and background <br> _Topics:_ Course outline, aspects of responsibility in data science through recent examples. <br> _Reading:_ <br> "Bias in Computer Systems", Friedman and Nissenbaum (1996) [ACM DL](https://dl.acm.org/citation.cfm?id=230561) <br> "Machine Bias", Angwin, Larson, Mattu, Kirchner (2016) [ProPublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) <br> "Data, Responsibly", Abiteboul and Stoyanovich (2015) [ACM SIGMOD blog](http://wp.sigmod.org/?p=1900) | [slides](https://dataresponsibly.github.io/courses/documents/spring19/Lecture1.pdf)  |  |
| Jan&nbsp;31 | **Lab:** ProPublica's Machine Bias | [jupyter notebook](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab_1.ipynb)    |  |
| Feb&nbsp;4  | **Lecture:** Fairness <br> _Topics:_ A taxonomy of fairness definitions; individual and group fairness. The importance of a socio-technical perspective: stakeholders and trade-offs. <br> _Reading:_ <br> "Big Data's Disparate Impact", Barocas and Selbst (2016) [pdf](http://www.californialawreview.org/wp-content/uploads/2016/06/2Barocas-Selbst.pdf) <br> “Fairness through awareness”, Dwork, Hardt, Pitassi, Reingold, Zemel (2012) [ACM DL](https://dl.acm.org/citation.cfm?doid=2090236.2090255) <br> "On the (im)possibility of fairness", Friedler, Scheidegger, Venkatasubramanian (2016) [arXiv](https://arxiv.org/abs/1609.07236) |  [slides](https://dataresponsibly.github.io/courses/documents/spring19/Lecture2.pdf)|  |
| Feb&nbsp;7  |**Lab:** IBM's AI Fairness 360 toolkit <br> _Reading:_ <br> "Data preprocessing techniques for classification without discrimination", Kamiran and Calders (2012) [pdf](https://link.springer.com/content/pdf/10.1007%2Fs10115-011-0463-8.pdf) | [jupyter notebook](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab2.ipynb) [slides](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab2.pdf) |  |
| Feb&nbsp;11 | **Lecture:** Fairness <br> _Topics:_ Impossibility results; causal definitions; fairness beyond classification. <br> _Reading:_ <br> "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments", Chouldechova (2017) [arXiv](https://arxiv.org/abs/1703.00056) <br> "Inherent Trade-Offs in the Fair Determination of Risk Scores", Kleinberg, Mullainathan, Raghavan (2017) [pdf](http://drops.dagstuhl.de/opus/volltexte/2017/8156/pdf/LIPIcs-ITCS-2017-43.pdf) <br> "Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions", Mitchell, Porash, Barocas (2018) [arXiv](https://arxiv.org/abs/1811.07867) |  [slides](https://dataresponsibly.github.io/courses/documents/spring19/Lecture3.pdf)|  |
| Feb&nbsp;14 | **Lab:** IBM's AI Fairness 360 toolkit <br> _Reading:_ <br> "Certifying and removing disparate impact", M. Feldman, S. A. Friedler, J. Moeller, C. Scheidegger, and S. Venkatasubramanian (2015) [pdf](https://arxiv.org/pdf/1412.3756.pdf) | [jupyter notebook](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab3.ipynb) [slides](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab3.pdf)  | HW1 assigned |
| Feb&nbsp;18 | No class, university holiday |  |  |
| Feb&nbsp;21 | **Lab:** Fairness and Causality |  [slides](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab4.pdf)|  |
| Feb&nbsp;25 | **Lecture:** Anonymity and privacy, guest lecture by [Daniela Hochfellner](https://cusp.nyu.edu/profiles/daniela-hochfellner/) <br> _Topics:_ Overview of responsible data sharing. Anonymization techniques; the limits of anonymization. Harms beyond re-identification.<br> _Reading:_ <br>"The Belmont Report" (1979) [pdf](https://www.hhs.gov/ohrp/sites/default/files/the-belmont-report-508c_FINAL.pdf) <br> "Critical questions for Big Data", danah boyd and Cate Crawford (2012) [pdf](https://www.tandfonline.com/doi/pdf/10.1080/1369118X.2012.678878) |  [slides](https://dataresponsibly.github.io/courses/documents/spring19/Lecture4.pdf) | HW1 due |
| Feb&nbsp;28 | **Lab:** Anonymity and privacy | [jupyter notebook](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab5.ipynb) [jupyter notebook brute force](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab5-Brute_force.ipynb) [slides](https://dataresponsibly.github.io/courses/documents/spring19/RDS_Lab5.pdf)  | |
| Mar&nbsp;4  | **Lecture:**  no class, snow day | |
| Mar&nbsp;7  | **Lab:** Anonymity and privacy (see Mar&nbsp;11 materials) |  | |
| Mar&nbsp;11 | **Lecture:** Anonymity and privacy <br> _Topics:_ Differential privacy; privacy-preserving synthetic data generation; exploring the privacy / utility trade-off. <br> _Reading:_ <br>"A firm foundation for private data analysis", C. Dwork (2011) [ACM DL](https://dl.acm.org/citation.cfm?doid=1866739.1866758)<br>"Can a set of equations keep U.S. census data private?", J. Mervis (2019) [Science](https://www.sciencemag.org/news/2019/01/can-set-equations-keep-us-census-data-private)  |  [slides](https://dataresponsibly.github.io/courses/documents/spring19/Lecture5.pdf) |  |
| Mar&nbsp;14 | **Lab:** Data Synthesizer<br> _Reading:_ <br>"DataSynthesizer: Privacy-Preserving Synthetic Datasets", Ping, Stoyanovich, howe (2017) [ACM DL](https://dl.acm.org/citation.cfm?doid=3085504.3091117)  |  | HW2 assigned |
| Mar&nbsp;18 | No class, university holiday |  |  |
| Mar&nbsp;21 | No class, university holiday |  |  |
| Mar&nbsp;25 | **Lecture:** Profiling and particularity, guest lecture by [Solon Barocas](http://solon.barocas.org/) <br> _Topics:_ Profiling and particularity<br>_Reading:_<br>"On individual risk", Dawid (2017) [pdf](https://link.springer.com/content/pdf/10.1007%2Fs11229-015-0953-4.pdf)<br>"We Are All Different: Statistical Discrimination and the Right to Be Treated as an Individual", Lippert-Rasmussen (2011) [pdf](https://link.springer.com/content/pdf/10.1007%2Fs10892-010-9095-6.pdf) |  |  |
| Mar&nbsp;28 | **Lab:** Data profiling |  | HW2 due |
| Apr&nbsp;1  | **Lecture:** Data profiling and data cleaning<br> _Topics:_ Overview of the data science lifecycle. Data profiling and validation. Qualitative and quantitative error detection. Missing attribute values and imputation. Outlier detection; duplicate detection. Documenting data cleaning transformations. |  | HW3 assigned |
| Apr&nbsp;4  | **Lab:** Data cleaning |  |  |
| Apr&nbsp;8  | **Lecture:** Transparency <br> _Topics:_ Auditing black-box models; explainable machine learning; software testing. |  | |
| Apr&nbsp;11 | **Lab:** LIME, Quantitative Input Influence |  | HW3 due<br> HW4 assigned |
| Apr&nbsp;15 | **Lecture:** From transparency to accountability <br> _Topics:_ Online price discrimination, transparency in online ad delivery. Transparency and accountability. Legal frameworks: GDPR and the right to explanation; NYC ADS transparency law. From auditing to interpretability. |  |  |
| Apr&nbsp;18 | **Lab:** Final review |  |  |
| Apr&nbsp;22 | **Lecture:** Final exam (in class) |  | HW4 due |
| Apr&nbsp;25 | **Lab:** Nutritional labels |  | Project assigned |
| Apr&nbsp;29 | **Lecture:** Diversity <br> _Topics:_ Background on diversity in information retrieval, recommender systems and crowdsourcing; diversity models and algorithms; diversity vs. fairness; trade-offs between diversity and utility. |  |  |
| May&nbsp;2  | **Lab:** Diversity |  |  |
| May&nbsp;6  | **Lecture:** Reproducibiilty |  |  |
| May&nbsp;9  | **Lab:** Reproducibility |  |  |
| May&nbsp;13 | **Lecture:** Project presentations |  | Project report due |
