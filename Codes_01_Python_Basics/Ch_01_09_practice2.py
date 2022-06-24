# %% [markdown]
# # About 
# This code has practice questions related to python basics.



# %% [markdown]
# # Libraries
# %% [code]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")



# %% [markdown]
# # Dataset
# %% [code]
tips = sns.load_dataset("tips")
tips.head()



# %% [markdown]
# # Q. Plot the distribution of `total_bill` in the given dataset.
# %% [code]
sns.displot(tips['total_bill'], kde=True)



# %% [markdown]
# # Q. Plot the destribution plot for tips.
# %% [code]
sns.displot(tips['tip'], kde=True)



# %% [markdown]
# # Q. Make a joint plot between `tip` and `total bill`.
# %% [code]
sns.jointplot(x=tips['total_bill'], y=tips['tip']);



# %% [markdown]
# # Q. Give additional attribute `kind = "hex"` in the above plot.
# %% [code]
sns.jointplot(x=tips['total_bill'], y=tips['tip'], kind = "hex");



# %% [markdown]
# # Q. Make pairplot between `total_bill` and `tip`.
# %% [code]
sns.pairplot(tips[['total_bill','tip']])



# %% [markdown]
# # Q. Make striplot between `sex` and `tip`.
# %% [code]
sns.stripplot(x=tips['sex'], y=tips['tip'])



# %% [markdown]
# # Q. Make bar plot with `day` and `total_bill`
# %% [code]
sns.barplot(x=tips['day'], y=tips['total_bill']);




# %% [markdown]
# # Q. Make a plot to count total males and females for each day.
# %% [code]
sns.countplot(x=tips['day'], hue = tips['sex'])




# %% [markdown]
# %% [code]
# # Q. Use factorplot to plot multiple categorical variables like day, smoker, peoplecount.
sns.factorplot(x = "day", y = "size", hue = "size", col = "smoker", data = tips, kind = "bar")



# %% [markdown]
# # Q. Use `lmplot()` to plot the relation between `total_bill` and `tip`
# %% [code]
sns.lmplot(x = "total_bill", y = "tip", data = tips);



# %% [markdown]
# # Q. In the above graph differentiate points for male and female.
# %% [code]
sns.lmplot(x = "total_bill", y = "tip", data = tips, hue = "sex");



# %% [markdown]
# # Q. Plot the above graph for smoker and non-smoker.
# %% [code]
sns.lmplot(x = "total_bill", y = "tip", data = tips, hue = "smoker")



# %%