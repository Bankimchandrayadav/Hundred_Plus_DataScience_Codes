# %% [markdown] 
# # About 
# This code is an extended exercise related to statistics.



# %% [markdown]
# 1. Import necessary packages
# %%
import pandas as pd
import numpy as np
import seaborn as sns
import os



# %% [markdown]
# 2. Load the file
# %%
inc_exp = pd.read_csv("../01_InFiles/Inc_Exp_Data.csv")



# %% [markdown]
# 3. Get the first 10 entries of the data
# %%
inc_exp.head(10)



# %% [markdown]
# 4. What is the Mean Expense of a Household?
# %%
inc_exp.Mthly_HH_Expense.mean()



# %% [markdown]
# 5. What is the Median Household Expense?
# %%
inc_exp.Mthly_HH_Expense.median()



# %% [markdown]
# 6. What is the Monthly Expense for most of the Households?
# %%
# Get the count of each value of monthly expense
mth_exp_tmp = pd.crosstab(index=inc_exp["Mthly_HH_Expense"], columns="count")
mth_exp_tmp
# %%
# Set index
mth_exp_tmp.reset_index(inplace=True)
mth_exp_tmp



# %% [markdown]
# ## 6.1 Getting all the column values of the row c/t max monthly expense
# %%
# Get the count of each value of monthly expense (just like pd.crosstab)
inc_exp.Mthly_HH_Expense.value_counts()
# %% 
# Max monthly expense value
inc_exp.Mthly_HH_Expense.value_counts().max()
# %% 
# Get the boolean array c/t max monthly expense
mth_exp_tmp['count'] == inc_exp.Mthly_HH_Expense.value_counts().max()
# %%
# Boolean array c/t max value
mth_exp_tmp[mth_exp_tmp['count'] == inc_exp.Mthly_HH_Expense.value_counts().max()]



# %% [markdown]
# 7. Plot a barchart to count the Highest qualified member
# %%
# Get value counts of each category of 'Highest_Qualified_Member' col
inc_exp['Highest_Qualified_Member'].value_counts()
# %%
# Plot
inc_exp['Highest_Qualified_Member'].value_counts().plot(kind='bar')



# %% [markdown]
# 8. Calculate IQR(difference between 75% and 25% quartile) for monthly income
# %%
# 75% quantile
inc_exp["Mthly_HH_Income"].quantile(0.75)
# %%
# 25% quantile
inc_exp["Mthly_HH_Income"].quantile(0.25)
# %%
# IQR
IQR = inc_exp["Mthly_HH_Income"].quantile(0.75) - inc_exp["Mthly_HH_Income"].quantile(0.25)
IQR



# %% [markdown]
# 9. Calculate Standard Deviation for first 4 columns.
# %%
# Std. dev. for first 4 cols
inc_exp.iloc[:,0:5].std()
# %%
# Present as a df
inc_exp.iloc[:,0:5].std().to_frame().T



# %% [markdown]
# 10. Calculate Variance for first 3 columns.
# %%
# Var for first 4 cols
inc_exp.iloc[:,0:4].var()
# %%
# Present as a df
pd.DataFrame(inc_exp.iloc[:,0:4].var().to_frame()).T



# %% [markdown]
# 11. Calculate the count of Highest qualified member.
# %%
# Counts
inc_exp['Highest_Qualified_Member'].value_counts()
# %%
# Present as a df
inc_exp['Highest_Qualified_Member'].value_counts().to_frame().T



# %% [markdown]
# 12.Plot the Histogram to count the No_of_Earning_Members
# %%
# Count
inc_exp['No_of_Earning_Members'].value_counts()
# %%
# Plot
inc_exp['No_of_Earning_Members'].value_counts().plot(kind='bar')



# %% [markdown]
# 13. Suppose you have option to invest in Stock A or Stock B. The stocks have different expected returns and standard deviations. The expected return of Stock A is 15% and Stock B is 10%. Standard Deviation of the returns of these 
# stocks is 10% and 5% respectively. Which is better investment?
# %%
# CV of stock A 
print('CV of stock A =', format(10/15, '.2f'))
# %%
# CV of stock B
print('CV of stock B =', 5/10)
# %% 
print('Stock B is a better investment')



# %%