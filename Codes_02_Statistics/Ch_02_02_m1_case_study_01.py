# %% [markdown]
# # About 
# This code is a case study available on kaggle (aimed at illustrating statistics)
# ### Case study - Understanding factors for Churn in a Telecom Company
# Source - https://www.kaggle.com/becksddf/churn-in-telecoms-dataset
# ### Context:
# 1. Predict behavior to retain customers. We can analyze all relevant customer data and develop focused customer retention programs.
# 2. Each row in the dataset represents a customer, and each column contains customer's attributes described on the column metadata.
# 3. The case study deals with exploratory data analysis.



# %% [markdown]
# # Data:
# The dataset is about telecom industry which tells about the number of customers who churned the service. It consists of 3333 observations having 21 features. We have to predict which customer is going to churn the service. The features are:
# 1. Account Length: how long account has been active.
# 2. VMail Message: Number of voice mail messages send by the customer.
# 3. Day Mins: Time spent on day calls.
# 4. Eve Mins: Time spent on evening calls.
# 5. Night Mins: Time spent on night calls.
# 6. Intl Mins: Time spent on international calls.
# 7. Day Calls: Number of day calls by customers.
# 8. Eve Calls: Number of evening calls by customers.
# 9. Intl Calls: Number of international calls.
# 10. Night Calls: Number of night calls by customer.
# 11. Day Charge: Charges of Day Calls.
# 12. Night Charge: Charges of Night Calls.
# 13. Eve Charge: Charges of evening Calls.
# 14. Intl Charge: Charges of international calls.
# 15. VMail Plan: Voice mail plan taken by the customer or not.
# 16. State: State in Area of study.
# 17. Phone: Phone number of the customer.
# 18. Area Code: Area Code of customer.
# 19. Intl Plan: Does customer have international plan or not.
# 20. CustServ Calls: Number of customer service calls by customer.
# 21. Churn : Customers who churned the telecom service or who doesn’t(0='Churner', 1='Non-Churner')



# %% [markdown]
# # Libraries
# %% [code]
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
import seaborn as sns



# %% [markdown]
# # Import the data
# %% [code]
ch = pd.read_csv('../01_InFiles/Churn.csv')



# %% [markdown]
# # How do we display the dataframe?
# %% [code]
ch



# %% [markdown]
# # Calculate Histogram for time spent on day calls by customers.
# %% [code]
plt.hist(ch['total day minutes'], bins= 10, facecolor= 'tan')
plt.xlabel('Total Day Minutes')
plt.ylabel('No. of Customers')
plt.show()



# %% [markdown]
# # How do we categorize the churner and the non-churner for the time spent on day
# calls (total day minutes)?
# %% [code]
g = sns.FacetGrid(ch, col="churn")
g.map(plt.hist, "total day minutes")



# %% [markdown]
# # Find the number of customers who did opt for voice mail plan
# %% [code]
ch['voice mail plan'].value_counts()



# %% [markdown]
# # Produce a countplot for the above result.
# %% [code]
sns.set(style="whitegrid", color_codes=True)
sns.countplot(data=ch, x="voice mail plan")
# %% [code]
# Categorized by churn or not churn
sns.countplot(data=ch, x="voice mail plan", hue= "churn")



# %% [markdown]
# # Create a boxplot for a categorical variable (international plan) and continuous variable (area code).
# %%
sns.boxplot(data=ch, x = "international plan", y = "area code")



# %% [markdown]
# # Create a crosstab for the area code to find the churner or non-churner.
# %%
pd.crosstab(ch['area code'], ch['churn'])



# %% [markdown]
# # How to pivot information using python for categorical values? Plot one.
# %%
pd.pivot_table(ch, index = ['area code','voice mail plan'], columns=['international plan'], aggfunc=len)



# %% [markdown]
# # Now calculate the total international minutes for all the combinations above. 
# %%
pd.pivot_table(ch, values='total intl minutes', index = ['area code','voice mail plan'], columns=['international plan'])



# %% [markdown]
# # How do we understand the correlation between the variables or the columns within the dataframe. Plot one and analyze.
# %%
plt.figure(figsize = (16,16));
corr = ch.corr();
sns.heatmap(corr, annot = True, cmap="Accent")



# %% [markdown]
# # Find Standard deviation of total night calls.
# %%
ch['total night calls'].std()



# %% [markdown]
# # Plot a distplot for the above result to look specifically at total night calls.
# %%
sns.displot(ch['total night calls'], kde=True);



# %% [markdown]
# # Plot a histogram to group it by churner or non-churner for the column area code.
# %%
ch.hist(by='churn', column = 'total night calls')



# %% [markdown]
# # Calculate areawise (area code wise) churner or non-churner using countplot.
# %%
ch['area code']= ch['area code'].astype('category')
sns.countplot(data=ch, x="area code", hue= "churn")



# %% [markdown]
# # That's all folks!