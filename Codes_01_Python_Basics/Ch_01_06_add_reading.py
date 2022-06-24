# %% [markdown]
# # About 
# This code is taken from one of the public blogs over pandas: [https://www.mygreatlearning.com/blog/python-pandas-tutorial](https://www.mygreatlearning.com/blog/python-pandas-tutorial)



# %% [markdown]
# # Libraries
# %% [code] 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



# %% [markdown]
# # Same aggregate function on all columns.
# %% [code]
# Define df
data = {'Name':['jennifer Lawrence', 'Brad Pitt', 'Chris Hemsworth', 'Dwayne Johnson'], 'Salary':[1000, 80000, 79000, 93000], 'Age':[33, 50, 45, 52]}
df = pd.DataFrame(data)
df
# Agg. function
df.aggregate(['sum','min','max','mean'], axis=0)



# %% [markdown]
# # Different aggregate functions for different columns
# %% [code]
df.aggregate({'Salary':['sum','mean'], 'Age':['min','max']})



# %% [markdown]
# # Groupby 
# %% [code]
# Firstly add a duplicate row to the last of df
df
df.loc[len(df.index)] = ['Dwayne Johnson', 85000, 54]  
# OR 
# df.loc[4] = ['Dwayne Johnson', 85000, 54]  # since len(df.index)=4
# df.iloc[len(df.index)] = ['Dwayne Johnson', 85000, 54]  # will throw error
df
# Now group 
g = df.groupby('Name')
# Access group properties
g.groups.keys()  
g.last(1)
g.get_group('Chris Hemsworth')



# %% [markdown]
# # Concatenating using `.append()` function
# %% [code]
# Define dataframes to append
data1 = {'Name':['Mercy', 'Prince', 'John', 'Cena'], 'Age':[27, 24, 22, 32],} 
data2 = {'Address':['Canada', 'UK', 'India', 'USA'], 'Qualification':['Btech', 'B.A', 'MS', 'Phd']}
df1 = pd.DataFrame(data1, index=['K0', 'K1', 'K2', 'K3'])
df2 = pd.DataFrame(data2, index=['K0', 'K1', 'K2', 'K3'])  
df1
df2
# Append
df1.append(df2)  



# %% [markdown]
# # Notes 
# 1. `.append()` function concatenates along axis = 0 only. It can take multiple objects as input.



# %% [markdown]
# # Generating random datetime
# %% [code]
# At hourly freq
pd.date_range(start='10/28/2011', periods = 5, freq ='H')
pd.date_range(start='01/06/2022', periods=5, freq='D')
# Specifying no. of samples b/w a range of date
pd.date_range(start='9/28/2018', end='10/28/2018', periods = 10)



# %% [markdown]
# # Notes 
# 1. The last line of above cells is equivalent to `np.linspace(start, stop, no. of samples)`.



# %% [markdown]
# # Conversion to timestamps
# %% [code]
# series 
sr1 = pd.Series(['Jul 04, 2020', '2020-10-28', '03/04/2022'])
pd.to_datetime(sr1) 
# string 
str1='4/7/2022'
pd.to_datetime(str1, format='%m/%d/%Y')  # mm/dd/yyy
pd.to_datetime(str1, format='%d/%m/%Y')  # dd/mm/yyy



# %% [markdown]
# # Dividing datetime into its features 
# %% [code]
# Define a df with timestamps
df = pd.DataFrame() 
df['date'] = pd.date_range('10/28/2020', periods = 10, freq ='H') 
df.head()
# Create features for year, month, day, hour, and minute 
df['year']  = df['date'].dt.year 
df['month'] = df['date'].dt.month 
df['day']   = df['date'].dt.day 
df['hour']  = df['date'].dt.hour 
df['minute'] = df['date'].dt.minute 
df.head()



# %% [markdown]
# # Line plot in pandas 
# %% [code]
# Define a df 
df = pd.DataFrame(data=np.random.randn(10,4), index=pd.date_range('2022-05-25',periods=10), columns=list('DBCY'))
df
# Plot 
df.plot()



# %% [markdown]
# # Bar plot in pandas 
# %% [code]
df = pd.DataFrame(np.random.rand(10,4),columns=list('abcd'))
df
# Regular
df.plot.bar()
df.a.plot.bar()
# Stacked
df.plot.bar(stacked=True)
df.plot.barh(stacked=True)



# %% [markdown]
# # Histogram 
# %% [code]
# Define dataframe
df =pd.DataFrame(
    data={'A':np.random.randn(100)-3, 'B':np.random.randn(100)+1, 'C':np.random.randn(100)+3, 'D':np.random.randn(100)-1}, 
    columns=['A', 'B', 'C', 'D'])
df
# Plot combined histogram
df.plot.hist(bins=20)
# Plot seperate histograms
df.hist(bins=20)
# Plot single histogram
df.A.hist(bins=20)



# %% [markdown]
# # Notes 
# 1. Commands such as `np.random.randn(100)-3` generate 100 random numbers under normal distribution, and subtract 3 from them.



# %% [markdown]
# # Scatter plot 
# %% [code]
df.plot.scatter(x='A', y='B')



# %% [markdown]
# # Pie chart
# %% [code]
df = pd.DataFrame(np.random.rand(5), index=list('ABCDE'))
df
df.plot.pie(subplots=True)



# %%