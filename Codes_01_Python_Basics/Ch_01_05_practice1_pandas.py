# %% [markdown]
# # About
# This code is a practice exercise related to pandas package.



# %% [markdown]
# # Libraries
# %% [code]
import numpy as np
import pandas as pd


# %% [markdown]
# # Background
# ## Why pandas when numpy?
# We have seen Numpy in the last section. It is good at performing math operations on 
# 2d-arrays of numbers. But the major drawback is, <u>it cannot deal with heterogenous values</u>. So, Pandas dataframes are helpful in that aspect for storing different data types and referring to these values like a dictionary instead of just referring each item with index.
# ## Series
# Pandas series are almost same as nd arrays in numpy, with the additional
# inferencing ability of custom labels like keys in a dictionary in python.
# %% [code]
# Regular syntax of defining a series
series1 = pd.Series(data = [1,2,3], index = ['key1', 'key2', 'key3'])
series1



# %% [markdown]
# # Question 1
# Convert a given dictionary to pandas series.
# %% [code]
d1 = {'a': 1, 'b': 2, 'c': 3}
series2 = pd.Series(d1)
series2



# %% [markdown]
# # Question 2
# Find the dot product of `series1` and `series2` created above.
# %% [code]
series1
series2
np.dot(series1, series2)



# %% [markdown]
# # Theory 
# A dataframe is a table with labelled columns which can hold different types of data 
# in each column. Example df is:
# %% [code]
d1 = {'a': [1,2,3], 'b': [3,4,5], 'c':[6,7,8] }
df1 = pd.DataFrame(d1)
df1
# %% [markdown] 
# # Question 3
# Select second row in the above dataframe df1.
# %% [code]
# Output as series
df1.iloc[1]  
df1.iloc[1,]  
df1.loc[1]  
df1.loc[1,]  
# Output as df
df1.iloc[[1,]]  
df1.loc[[1,]]  



# %% [markdown]
# # Question 4
# Select column `c` in second row of `df1`. </br>
# Hint: For using labels use `df.loc[row, column]`. For using numeric indices use `df.iloc[]`. 
# %% [code]
df1
df1.loc[1,'c']
# df1.loc[[1,'c']]  # will throw error



# %% [markdown]
# # Question 5
# Check the type and dimensions of given dataset - `mtcars`.
# ## Background 
# 1. For the below set of questions, we will be using the cars data from Motor Trend Car Road Tests - [http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html](http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html). </br>
# 2. The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973-74 models). 
# 3. Details:
# - A data frame with 32 observations on 11 (numeric) variables.
# - `mpg`:	Miles/(US) gallon
# - `cyl`:	Number of cylinders
# - `disp`:	Displacement (cu.in.)
# - `hp`:	Gross horsepower
# - `drat`:	Rear axle ratio
# - `wt`:	Weight (1000 lbs)
# - `qsec`:	1/4 mile time
# - `vs`:	Engine (0 = V-shaped, 1 = straight)
# - `am`:	Transmission (0 = automatic, 1 = manual)
# - `gear`:	Number of forward gears
# - `carb`:	Number of carburetors 
# %% [code]
# Reading the dataset from a csv file using pandas.
mtcars = pd.read_csv('../01_InFiles/mtcars.csv')
mtcars.head()
mtcars.set_index('model', drop=True, inplace=True)
# Type of
type(mtcars)
mtcars.dtypes
# Dimensions
mtcars.shape



# %% [markdown]
# # Question 6
# Check the first 10 lines and last 10 lines of the given dataset - `mtcars`.
# %% [code]
mtcars.head(10)
mtcars.tail(10)



# %% [markdown]
# # Question 7
# Print all the column labels in the given dataset - `mtcars`.
# %% [code]
mtcars.columns



# %% [markdown]
# # Question 8
# Select first 6 rows and 3 columns in the `mtcars` dataframe.
# %% [code]
mtcars.head()
mtcars.iloc[:6,:3]



# %% [markdown]
# # Question 9
# Select the rows from `Mazda RX4` to `Valiant` in the `mtcars` dataset and display 
# only `mpg` and `cyl` values of those rows. 
# %% [code]
mtcars.loc['Mazda RX4':'Valiant', ['mpg','cyl']]



# %%