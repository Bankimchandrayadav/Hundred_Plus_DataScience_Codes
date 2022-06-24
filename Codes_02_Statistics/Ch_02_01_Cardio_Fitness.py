# %% [markdown]
# # Cardio Good Fitness Case Study - Descriptive Statistics
# The market research team at AdRight is assigned the task to identify the profile of the typical customer for each treadmill product offered by CardioGood Fitness. The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics. The team decides to collect data on individuals who purchased a treadmill at a CardioGoodFitness retail store during the prior three months. The data are stored in the CardioGoodFitness.csv file.
# 
# ### The team identifies the following customer variables to study: 
#   - product purchased, TM195, TM498, or TM798; 
#   - gender; 
#   - age, in years; 
#   - education, in years; 
#   - relationship status, single or partnered; 
#   - annual household income ; 
#   - average number of times the customer plans to use the treadmill each week; 
#   - average number of miles the customer expects to walk/run each week; 
#   - and self-rated fitness on an 1-to-5 scale, where 1 is poor shape and 5 is excellent shape.
# 
# ### Perform descriptive analytics to create a customer profile for each CardioGood Fitness treadmill product line.



# %% [markdown]
# Libraries
# %% [code]
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline



# %% [markdown]
# Load the Cardio Dataset 
# %% [code]
mydata = pd.read_csv('../01_InFiles/CardioGoodFitness.csv')
mydata.head()



# %% [markdown]
# # Notes 
# 1. Data types:
#   - Product column has nominal data.   
#   - Age: Numerical and ordered. 
#   - Gender: Nominal
#   - Education: Quantitative ordered variable. 
#   - Marital status: Nominal.
#   - Usage: Numerical and ordered
#   - Fitness: Ordinal
# 2. Here, we can note that the scale of income and fitness are far apart. 



# %% [markdown]
# # Basic info
# %% [code]
mydata.describe(include="all")



# %% [markdown]
# # Notes 
# 1. The nominal variable `Product` has 180 observations with 3 different types and the type TM195 as the one occuring most often (80 times). No quantitative measures are possible. Similar statistical summaries are generated for `Gender` and `Marital Status`. 
# 2. `Age` and other elements too have 180 observations. Here, the number of unique observations of Age do not make since Age is a continuous variable in the df, and is not reported by python. We get to know that the youngest person in our data is 18 yrs old and the eldest is 50 yrs old. Half of the people are more than 26 and half are less than 26. In terms of quartiles, a quarter of the people are less than 24, and a quarter are more than 33, and half the people are between 24 and 33. The IQR s 33-24=9. The range is 50-32=18. Mean age (~29) is a little more than the median (26) signifying a longer tail to the right. i.e. right skewed which pushes the mean to be larger than the median. Further 2/3 rds of the data lies in the range 28.8 +/- 7.
# 3. Similar statistical summaries are generated for `Education`, `Usage`, `Fitness` and `Income`. 
# 4. In this case, the no. of variabels are not much and fits easily onto the computer screen. 



# %% [markdown]
# # Basic info [contd.]
# %% [code]
mydata.info()
# %% [markdown]
# # Notes 
# 1. Above gives details about the 'kinds' of numbers that are available in each of the variables. `Product` is an object which is python's version of saying that its categorical data that can be counted but not do arithmetic with. 
# 2. and `Age` is an integer stored in 64 bits over which arithmetics can be done such as std. dev., mean, etc. 



# %% [markdown]
# # Histogram
# %% [code]
mydata.hist(figsize=(20,30));



# %% [markdown]
# # Notes 
# 1. Histograms give a summary of the distribution and are automatically prepared for the variables for which it makes sense like Age, Income, etc.
# 2. Income has a bimodal shape. Mode is around 50,000 but there seems to be another baby distribution at the higher income level with its own baby peak or mode. Clustering algorithms often allow the seperation of data in such cases, and a histogram is a leading indicator of such a situation.



# %% [markdown]
# # Boxplot
# %% [code]
sns.boxplot(x="Gender", y="Age", data=mydata);
sns.boxplot(x="Product", y="Age", data=mydata);



# %% [markdown]
# # Cross tabulation
# %% [code]
pd.crosstab(mydata['Product'],mydata['Gender'] )
pd.crosstab(mydata['Product'],mydata['MaritalStatus'])



# %% [markdown]
# # Notes 
# 1. `pd.crosstab` is applicable when both the variables are categorical.
# 2. How the 180 observations when categorized through gender/marital status and product are distrbuted. 
# 3. This same information can also be represented by means of `.countplot()` as seen in next cell.



# %% [markdown]
# # Count plot
# %% [code]
sns.countplot(x="Product", hue="Gender", data=mydata)



# %% [markdown]
# # Pivot table
# %% [code]
pd.pivot_table(mydata, index=['Product', 'Gender'], columns=[ 'MaritalStatus'], aggfunc=len)
pd.pivot_table(mydata,'Income', index=['Product', 'Gender'], columns=['MaritalStatus'])
pd.pivot_table(mydata,'Miles', index=['Product', 'Gender'], columns=[ 'MaritalStatus'])



# %% [markdown]
# # Pairplot
# %% [code]
sns.pairplot(mydata)



# %% [markdown]
# # Notes 
# 1. A pairplot is an <u>array of plots</u>. 



# %% [markdown]
# # Basic stats
# %% [code]
mydata['Age'].std()
mydata['Age'].mean()
sns.displot(mydata['Age'], kde=True);



# %% [markdown]
# # Comparative Histograms [imp.]
# %% [code]
mydata.hist(by='Gender',column = 'Age');
mydata.hist(by='Gender',column = 'Income');
mydata.hist(by='Gender',column = 'Miles');
mydata.hist(by='Product',column = 'Miles', figsize=(20,30));



# %% [markdown]
# # Correlation coefficient and Covariance
# %% [code]
# Correlation coefficient
mydata.corr()
# Covariance
mydata.cov()


# %% [markdown]
# # Notes 
# 1. Correlation coefficient is the normalized version of Covariance. 
# 2. Cols such as income, with large nos. are better understood in terms of corr coeff. Also, corr coeff generates values for all cols in the same range i.e., `-1` to `+1`, making it much easier to interpret than covariance.



# %% [markdown]
# # Visual representation of correlation matrix
# %% [code]
sns.heatmap(mydata.corr(), annot=True)



# %% [markdown]
# # Simple Linear Regression
# %% [code]
# Load function from sklearn
from sklearn import linear_model
# Create linear regression object
regr = linear_model.LinearRegression()
# Set X and y
X = mydata[['Usage','Fitness']]
y = mydata['Miles']
# Train the model using the training sets
regr.fit(X,y)



# %% [markdown]
# # Regression stats
# %% [code]
regr.coef_
regr.intercept_



# %% [markdown]
# # Notes
# 1. Relation obtained is :MilesPredicted = -56.74 + 20.21*Usage + 27.20*Fitness
# 2. The above relation obtained between X('Usage', 'Fitness') and y('Miles') shows that for the same level of fitness a unit increase, 1 unit increase in usage leads to 20 units increase in miles.



# %% [markdown]
# # The end.