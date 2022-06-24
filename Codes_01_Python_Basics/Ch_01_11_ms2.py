# %% [markdown]
# # About 
# This code is a public case study available on kaggle - to illusrate python basics (numpy and pandas).
# ### Case Study - Honey Production
# 
# Source Credit : https://www.kaggle.com/jessicali9530/honey-production
# 
# #### Context
# In 2006, global concern was raised over the rapid decline in the honeybee population, an integral component to American honey agriculture. Large numbers of hives were lost to Colony Collapse Disorder, a phenomenon of disappearing worker bees causing the remaining hive colony to collapse. Speculation to the cause of this disorder points to hive diseases and pesticides harming the pollinators, though no overall consensus has been reached. Twelve years later, some industries are observing recovery but the American honey industry is still largely struggling. The U.S. used to locally produce over half the honey it consumes per year. Now, honey mostly comes from overseas, with 350 of the 400 million pounds of honey consumed every year originating from imports. This dataset provides insight into honey production supply and demand in America by state from 1998 to 2012.
# 
# #### Content
# The National Agricultural Statistics Service (NASS) is the primary data reporting body for the US Department of Agriculture (USDA). NASS's mission is to "provide timely, accurate, and useful statistics in service to U.S. agriculture". From datasets to census surveys, their data covers virtually all aspects of U.S. agriculture. Honey production is one of the datasets offered. Click here for the original page containing the data along with related datasets such as Honey Bee Colonies and Cost of Pollination. Data wrangling was performed in order to clean the dataset. honeyproduction.csv is the final tidy dataset suitable for analysis. The three other datasets (which include "honeyraw" in the title) are the original raw data downloaded from the site. They are uploaded to this page along with the "Wrangling The Honey Production Dataset" kernel as an example to show users how data can be wrangled into a cleaner format. Useful metadata on certain variables of the honeyproduction dataset is provided below:
# 
#   - numcol: Number of honey producing colonies. Honey producing colonies are the maximum number of colonies from which honey was taken during the year. It is possible to take honey from colonies which did not survive the entire year
#   - yieldpercol: Honey yield per colony. Unit is pounds
#   - totalprod: Total production (numcol x yieldpercol). Unit is pounds
#   - stocks: Refers to stocks held by producers. Unit is pounds
#   - priceperlb: Refers to average price per pound based on expanded sales. Unit is dollars.
#   - prodvalue: Value of production (totalprod x priceperlb). Unit is dollars.
#   - Other useful information: Certain states are excluded every year (ex. CT) to avoid disclosing data for individual operations. Due to rounding, total colonies multiplied by total yield may not equal production. Also, summation of states will not equal U.S. level value of production.
# 
# 
# #### Acknowledgements
# Honey production data was published by the National Agricultural Statistics Service (NASS) of the U.S. Department of Agriculture. The beautiful banner photo was by Eric Ward on Unsplash.
# 
# #### Inspiration
#    - How has honey production yield changed from 1998 to 2012?
#    - Over time, which states produce the most honey? Which produce the least? Which have experienced the most change in honey yield?
#    - Does the data show any trends in terms of the number of honey producing colonies and yield per colony before 2006, which was when concern over Colony Collapse Disorder spread nationwide?
#    - Are there any patterns that can be observed between total honey production and value of production every year?
#    - How has value of production, which in some sense could be tied to demand, changed every year?



# %% [markdown]
# # Import pandas, numpy, seaborn, matplotlib.pyplot packages
# %% [code]
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline



# %% [markdown]
# # Import the honeyproduction.csv file
# %% [code]
mydata = pd.read_csv("../01_InFiles/honeyproduction.csv")



# %% [markdown]
# # Explore the data for non-null and extreme values
# %% [code]
mydata.head()
mydata.describe().transpose()
mydata.info()



# %% [markdown]
# # How many States are included in the dataset?
# %% [code]
mydata['state'].nunique()



# %% [markdown]
# # Which are the States that are included in this dataset?
# %% [code]
mydata['state'].unique()



# %% [markdown]
# # Calculate the average production for each state across all years
# %% [code]
mydata[['state', 'totalprod']].groupby('state').mean().round()



# %% [markdown]
# # Hw many years data is provided in the dataset? And what is the starting and ending year?
# %% [code]
mydata['year'].nunique()
mydata['year'].min()
mydata['year'].max()



# %% [markdown]
# # Which State has seen highest volume in production, and in which year?
# %% [code]
mydata[mydata['totalprod'] == mydata['totalprod'].max()]



# %% [markdown]
# # What is the average yield per colony , for each year?
# %% [code]
mydata[['year', 'yieldpercol']].groupby('year').mean().round()



# %% [markdown]
# # Is there correlation between any 2 Numeric variables? Test for the same using Visual techniques
# %% [code]
# Pairplot
sns.pairplot(mydata[['numcol', 'yieldpercol', 'totalprod', 'stocks', 'priceperlb', 'prodvalue']]);
# Stats
cor = mydata[['numcol', 
              'yieldpercol', 
              'totalprod', 
              'stocks', 
              'priceperlb', 
              'prodvalue']].corr()


# %% [markdown]     
# ## Heatmap of correlation
# %% [code]
sns.heatmap(cor,annot=True,cmap='plasma',vmin=-1,vmax=1)



# %% [markdown]
# # What is the general Production trend from 1998 to 2012? Describe visually
# %% [code]
sns.pointplot(mydata['year'], mydata['totalprod'])



# %% [markdown]
# # How is the production trend for each State? Describe visually - Hint 
# (Use `sns.FacetGrid()` & `g.map()` functions)
# %% [code]
g = sns.FacetGrid(mydata, col="state", col_wrap=5, height=3)
g = g.map(plt.plot, "year", "totalprod", marker=".")



# %% [markdown]
# # Is there a linear relationship between the Number of Colonies & Value in Production? 
# Check at an overall level, at state and year levels as well
# %% [code]
sns.lmplot(x="numcol", y="prodvalue", data=mydata)
sns.lmplot(x="numcol", y="prodvalue", data=mydata, hue='state')
sns.lmplot(x="numcol", y="prodvalue", data=mydata, hue='year')



# %% [markdown]
# # Interactive scatter plot using plotly package
# %% 
import plotly.express as px
px.scatter(mydata, x = 'numcol', y = 'prodvalue', animation_frame = 'year', size = 'totalprod')



# %% [markdown]
# # Check the distribution of total prodcution across each year using boxplots
# %% [code]
fig, ax = plt.subplots(figsize=(20,10))
sns.boxplot(x='year',y='totalprod',data=mydata)



# %% [markdown]
# # How has the Value in Production changed over the years?
# %% [code]
sns.pointplot(mydata['year'], mydata['prodvalue'])



# %% [markdown]
# # What is the linear relationship between Production volume & value over the years?
# %% [code]
sns.lmplot(x="totalprod", y="prodvalue", data=mydata)



# %%