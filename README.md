![housing market](https://github.com/lskerrett/Covid-and-Real-Estate-Canada/blob/master/Resources/housing%20market.jpg)


# **Modelling housing market during COVID-19**

Links to Google Slides:

- [Project presentation](https://docs.google.com/presentation/d/1XloGJetDxiyN7Yh3OSNy-hipRLcIVP5_HimekSp4Ru0/edit?usp=sharing)

- [Dashboard (Blueprint)](https://docs.google.com/presentation/d/1xjqhkGYUn4ZUA-6dhtKq79eNqyQp06-95V_FGOHLePA/edit?usp=sharing)

## **1._Description of the project** <br>
<br>

### *Overview*<br>
In Canada, the job market is remarkably concentrated in the big cities of the provinces across the country. This situation leads to higher demand of real state and rent activity in such cities, and many developers rely on such predictable outcome to invest. However, the economy in 2020 has been deeply affected by the COVID-19 pandemic which forced many to work from home, being no longer necessary to look for lodging in the big cities. In this situation, it is important for private developers to know if COVID-19 has affected significantly the housing market in big and small cities across Canada. We are aiming to provide insight on how much the house price index has changed in the months of the pandemic, by developing a tool to visualize the values in the pandemic months compared to the "business-as-usual" values which we predict by modeling using a machine learning algorithm approach.
<br>
<br>
### *The questions we hope to answer are: <br>*

- Did the real state market was impacted positively or negatively by COVID-19?
- Is the impact different in small cities and big cities?
<br>

### *Data sources: <br>*

We will use data from 3 differents sources: <br>

- [Canadian Mortgage and Housing Corporation](https://www.cmhc-schl.gc.ca/en/data-and-research) <br>
- [Statistics Canada](https://www150.statcan.gc.ca/n1/en/type/data?subject_levels=46) <br>
- [Canadian Real Estate Association](https://creastats.crea.ca/en-CA/) <br>
<br>

### *Data base samples:*
Housing inventory (housing_inventory_clean.csv) <br>
New housing prices (price_index_clean.csv) <br>
Canadian population 2011-2016 (cleaned_canada_pop_2011_2016.csv)<br>
<br>
### *Communication*

Communication will be done via Slack and Zoom. We will carry out online meetings at least twice a week with all members.
<br>
<br>
<br>
## **2._Process**<br>
<br>

A combination of unsupervised and supervised machine learning techniques will be used to gain a better understanding of the impact that Covid-19 has had on the real estate market. Unsupervised machine learning will be used to first identify any strong relationships between features, and then supervised machine learning will be used to build a model which predicts the housing price index for a particular city. This trained supervised machine learning model will then be used to predict potential cities that have high chances of having their housing price index increase. <br>
<br>
### **Part 1: Unsupervised machine learning**
<br>

### *Model characteristics:*

-**Dependent variable:** House price index <br>

-**Independent variables** (categorical variables were encoded): <br>
Housing Type (Land or Home), Price Index, Population Density, Year.<br>

-**Model algorithm**: K-means <br>
<br>
### *Analysis of results*

Two separate analyses were performed using unsupervised machine learning. One was performed for the value or price index for land, and the other for home vales or price index. Clusters were not clearly identified in the 3D plots for the two analyses, however it can be seen that a shift towards medium sized cities has been taking place over the past few years, and has been exacerbated in 2020. To improve this analysis, more features, such as city economic health factors should be considered. 

![Unsupervised machine learning result visualization - Land](/Resources/Unsupervised_ML_plot_land.PNG)
<br>
<br>
![Unsupervised machine learning result visualization - Home](/Resources/Unsupervised_ML_plot_housing.PNG)
<br>
<br>
### **Part 2: Supervised machine learning**
<br>
Supervised machine learning (Neural Networks) were used to initially build a model, but due to the low accuracy of the preliminary models, a simpler supervised machine learning technique such as multiple variable linear regression was chosen. Low fit factors were obtained, implying that this although better than neural networks, still don't accurately depict a relationship between the features and the dependent variable (Price Index). As mentioned above, further features need to be considered to improve the models accuracy.

![Supervised machine learning result summary - Land](/Resources/Supervised ML_Summary_Land.PNG)
<br>
<br>
![Supervised machine learning result summary - Home](/Resources/Supervised ML_Summary_Housing.PNG)
<br>
<br>
