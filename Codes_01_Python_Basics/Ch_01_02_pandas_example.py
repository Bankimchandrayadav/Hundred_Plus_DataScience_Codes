# %% [markdown]
# # About
# This code is a demonstration of the functionalities of a pandas dataframe.



# %% [markdown]
# # Libs
# In general it's good practice to import all pacakages at the beginning.
# %% [code]
import pandas as pd
import numpy as np  # not necessary for pandas



# %% [markdown]
# # Creating a series
# %% [code]
# From a list
mylist = [5.4,6.1,1.7,99.8]
myseries1 = pd.Series(data=mylist)
print(myseries1, '\n')
# From an array
myarray = np.array(mylist)
myseries2 = pd.Series(data=myarray)
print(myseries2, '\n')



# %% [markdown]
# # Access entries the same way as with lists or arrays
# %% [code]
print(myseries1[2], '\n')



# %% [markdown]
# # Replace index by custom labels
# %% [code]
mylabels = ['first','second','third','fourth']
myseries3 = pd.Series(data=mylist,index=mylabels)
print(myseries3, '\n')



# %% [markdown]
# # When not using keywords, order of entries is imp
# %% [code]
# First arg is expected to be data
myseries4 = pd.Series(mylabels, mylist)
print(myseries4, '\n')
myseries4 = pd.Series(mylist,mylabels)
print(myseries4, '\n')



# %% [markdown]
# # Access values with the custom labels
# %% [code]
print(myseries4['second'])



# %% [markdown]
# # We can do math on series 
# %% [code]
myseries5 = pd.Series([5.5,1.1,8.8,1.6],['first','third','fourth','fifth'])
print(myseries5, '\n')
print(myseries5+myseries4)



# %% [markdown]
# # Notes
# 1. The addition is performed with corresponding indices. 
# 2. Also, note that in doing the above addition, the labels of the new series were sorted alphabetically. 



# %% [markdown]
# # Creating a dataframe - combine series 
# %% [code]
# Stack col by col (axis=1) and don't sort 
df1 = pd.concat([myseries4,myseries5],axis=1,sort=False) 
df1
# Stack col by col (axis=1) and sort 
df1 = pd.concat([myseries4,myseries5],axis=1,sort=True)  
df1
# Stack row by row (axis=0) and don't sort 
df1 = pd.concat([myseries4,myseries5],axis=0,sort=False)
df1
# Stack row by row (axis=0) and don't sort 
df1 = pd.concat([myseries4,myseries5],axis=0,sort=True)
df1



# %% [markdown]
# # Notes 
# 1. Stacking row by row results into a new series as its still just a single column of a dataframe.
# 2. A very important point to note here is that when we are stacking col by col, the `sorting=False/True` is applicable over the index labels. 
# 3. Similarly, when we are stacking row by row, `sorting=False/True` is applicable over the column labels.




# %% [markdown]
# # Creating dataframe - from random numbers
# %% [code]
df2 = pd.DataFrame(np.random.randn(5,5))
df2
# Can give explicit labels while defining
df3 = pd.DataFrame(np.random.randn(5,5),index=['first row','second row','third row','fourth row','fifth row'], columns=['first col','second col','third col','fourth col','fifth col'])
df3



# %% [markdown]
# # Accessing cols by labels
# %% [code]
# Single
print(df3['second col'], '\n')
# Multiple
df3[['third col','first col']]



# %% [markdown]
# # Access rows by labels
# %% [code]
df3.loc['fourth row']



# %% [markdown]
# # Access rows by index
# %% [code]
df3.iloc[3]



# %% [markdown]
# # Access row and col together by labels
# %% [code]
df3.loc[['fourth row','first row'],['second col','third col']]



# %% [markdown]
# # Logical indexing for dataframes just like for numpy arrays
# %% [code]
df3>0
print(df3[df3>0])



# %% [markdown]
# # Notes 
# 1. Unlike matrices, logical indexing in dataframes doesn't result in a one dimensional array, and the structure of the dataframe is preserved. 
# 2. NaNs are showed at the False locations.



# %% Add columns to a dataframe
df3['sixth col'] = np.random.randn(5,1)
df3



# %% [markdown]
# # Remove rows from a dataframe
# %% [code]
df5 = df3.drop('second row',axis=0)
df5



# %% [markdown]
# # Remove columns from a dataframe
# %% [code]
df4 = df3.drop('first col',axis=1)
df4



# %% [markdown]
# # Remove columns from a dataframe
# %% [code]
df3.drop('first col',axis=1,inplace=True)
df3



# %% [markdown]
# # Notes
# 1. `df.drop()` doesn't change the original dataframe. It is just a function that takes a dataframe as input, and returns a modified dataframe.
# 2. In order to change the original dataframe, assign the output of the above function to a new variable like `df4` (or even `df3`), or use `inplace=True`. 



# %% [markdown]
# # We can remove a dataframe's index labels
# %% [code]
df5.reset_index(inplace=True)
df5



# %% [markdown]
# # We can assign new names to the index
# %% [code]
# Add a new col
df5['new name'] = ['This','is','the','row']
df5
# Set this col as index
df5.set_index('new name',inplace=True)
df5



# %% [markdown]
# # Combining data frames
# The ways dataframes are combined in pandas is similar to SQL.
# We will examine 3 methods for combining dataframes:
# 1. concat
# 2. join
# 3. merge



# %% Firstly define two dataframes
df7 = pd.DataFrame({"customer":['101','102','103','104'], 
                    'category': ['cat2','cat2','cat1','cat3'],
                    'important': ['yes','no','yes','yes'],
                    'sales': [123,52,214,663]},)
df8 = pd.DataFrame({"customer":['101','103','104','105'], 
                    'color': ['yellow','green','green','blue'],
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]})



# %% [markdown]
# # Concatenate
# %% [code]
# Stack row by row (axis=1) and don't sort 
pd.concat([df7,df8],axis=0,sort=False)
# Stack row by row (axis=1) and sort 
pd.concat([df7,df8],axis=0,sort=True)
# Stack col by col (axis=1) and don't sort
pd.concat([df7,df8],axis=1,sort=False)
# Stack col by col (axis=1) and sort
pd.concat([df7,df8],axis=1,sort=True)



# %% [markdown]
# # Notes
# 1. When we are stacking row by row (axis=0), `sorting=False/True` is applicable over the column labels. 
# 2. Similarly, when we are stacking col by col (axis=1), `sorting=False/True` is applicable over the index labels.
# 3. In the above example of stacking row by row, the common cols get values throughout their length, while the uncommon cols show NaN for one or the other df.



# %% [markdown]
# # Try above concat with dfs having different indices
# %% [code]
df7 = pd.DataFrame({"customer":['101','102','103','104'], 
                    'category': ['cat2','cat2','cat1','cat3'],
                    'important': ['yes','no','yes','yes'],
                    'sales': [123,52,214,663]},index=[0,1,2,3])
df8 = pd.DataFrame({"customer":['101','103','104','105'], 
                    'color': ['yellow','green','green','blue'],
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])


# %% [markdown]
# # Concatenate                
# %% [code]
# Stack row by row (axis=1) and don't sort 
pd.concat([df7,df8],axis=0,sort=False)
# Stack row by row (axis=1) and sort 
pd.concat([df7,df8],axis=0,sort=True)
# Stack col by col (axis=1) and don't sort
pd.concat([df7,df8],axis=1,sort=False)
# Stack col by col (axis=1) and sort
pd.concat([df7,df8],axis=1,sort=True)



# %% [markdown]
# # Notes 
# 1. Here the the two dataframes had different indices and upon concatenation by axis=0 produces results similar to when the dfs had same indices. 
# 2. But, when concatenating by axis=1, the results are much different that what they were when the dfs had common index. This time the upper left portion = `df7`, and the lower right portion = `df8`. Futher sorting=False/True is not changing the result since the indices are already sorted as `df7` had indices 0,1,2,3 and `df8` had indices 4,5,6,7. 



# %% [markdown]
# # Try the above concat with more variations 
# This time the dfs won't have sorted indices and also a common index.
# %% [code]
df7 = pd.DataFrame({"customer":['101','102','103','104'], 
                    'category': ['cat2','cat2','cat1','cat3'],
                    'important': ['yes','no','yes','yes'],
                    'sales': [123,52,214,663]},index=[4,5,6,7])
df8 = pd.DataFrame({"customer":['101','103','104','105'], 
                    'color': ['yellow','green','green','blue'],
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[0,1,2,4])


# %% [markdown]           
# # Concatenate
# %% [code]
# Stack row by row (axis=1) and don't sort 
pd.concat([df7,df8],axis=0,sort=False)
# Stack row by row (axis=1) and sort 
pd.concat([df7,df8],axis=0,sort=True)
# Stack col by col (axis=1) and don't sort
pd.concat([df7,df8],axis=1,sort=False)
# Stack col by col (axis=1) and sort
pd.concat([df7,df8],axis=1,sort=True)



# %% [markdown]           
# # Notes 
# 1. In first one: the common cols had values filled throught the df.
# 2. In second one: exactly the same as above, but he cols are sorted.
# 3. In third one: the no. of cols are one less in the concatenation of the previous variant of `df7` and `df8`. This time the index 4 has values filled up all along the row, as it is common to both the dfs.
# 4. In fourth one: same as above with 7 rows, but sorted indices.



# %% [markdown]
# Merge 
# 1. Merge combines dataframes using a column's values to identify common entries. 
# 2. For merge a very handy tip is: `on` decides which col and `how` decides which rows to keep.
# %% [code]
# Firstly define the dataframes:
df7 = pd.DataFrame({"customer":['101','102','103','104'], 
                    'category': ['cat2','cat2','cat1','cat3'],
                    'important': ['yes','no','yes','yes'],
                    'sales': [123,52,214,663]},index=[0,1,2,3])
df8 = pd.DataFrame({"customer":['101','103','104','105'], 
                    'color': ['yellow','green','green','blue'],
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])



# %% [markdown]
# # Merge - with common col names
# %% [code]
# Outer (union)
pd.merge(df7,df8,how='outer',on='customer') 
# Inner (intersection)
pd.merge(df7,df8,how='inner',on='customer') 
# Left
pd.merge(df7,df8,how='left',on='customer') 
# Right
pd.merge(df7,df8,how='right',on='customer') 



# %% [markdown]
# # Notes 
# ## Outer: 
# 1. Customers common to both dfs are: 101, 103 and 105. Hence, they have values all throughout the row of the merged df. 
# 2. Customer 102 is not present in df8, hence shows NaN under the cols of df8. Similarly, customer 105 is not present in df7, and shows NaN under the cols of df7. 
# 3. The columns with same names (`sales`) are automatically differentiated by the suffices `_x` and `_y` to represent which col belong to which df.
# ## Inner:
# 1. Only the rows/cells common to both the `customer` cols of the two dfs are preserved. Hence, only the customers 101, 103 and 104 are preserved.
# 2. This one won't showup any NaNs.
# ## Left: 
# 1. Here only the rows/cells of the `customer` col of df7 are preserved. 
# 2. This one can also show NaNs. As 102 is not present in df8, its values under the cols of df8 are shown NaN.
# ## Right:
# 1. Here only the rows/cells of the `customer` col of df8 are preserved. 
# 2. This one can also show NaNs. As 105 is not present in df7, its values under the cols of df7 are shown NaN.



# %% [markdown]
# # Merge - with different col names
# %% [code]
# Define dataframes
df7 = pd.DataFrame({"customer1":['101','102','103','104'], 
                    'category': ['cat2','cat2','cat1','cat3'],
                    'important': ['yes','no','yes','yes'],
                    'sales': [123,52,214,663]},index=[0,1,2,3])
df8 = pd.DataFrame({"customer2":['101','103','104','105'], 
                    'color': ['yellow','green','green','blue'],
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])



# %% [markdown]
# # Merge
# %% [code]
# Outer (union)
pd.merge(df7,df8,left_on='customer1',right_on='customer2',how='outer')
# Inner (intersection)
pd.merge(df7,df8,left_on='customer1',right_on='customer2',how='inner')
# Left
pd.merge(df7,df8,left_on='customer1',right_on='customer2',how='left')
# Right
pd.merge(df7,df8,left_on='customer1',right_on='customer2',how='right')



# %% [markdown]
# # Notes 
# 1. Everything behaves the same - outer, inner, left or right join, just the different col names of the dfs being merged are preserved in the resulting merged dataframe.
# 2. Its just that one col increases w.r.t the case when the dfs had a common col name.



# %% [markdown]
# # Join
# 1. Join does exactly the same thing as merge except that instead of using column values, it uses the index labels to identify common entries.
# 2. It can be thought of as if the two columns considered in a merge operation, are the index cols of the two dataframes.
# %% [code]
# Firstly define two dataframes to try join operations:
df9 = pd.DataFrame({'Q1': [101,102,103],
                    'Q2': [201,202,203]},
                   index=['I0','I1','I2'])

df10 = pd.DataFrame({'Q3': [301,302,303],
                    'Q4': [401,402,403]},
                   index=['I0','I2','I3'])



# %% [markdown]
# # Join operations
# %% [code]
df9.join(df10,how='outer') 
df9.join(df10,how='inner') 
df9.join(df10,how='left') 
df9.join(df10,how='right') 



# %% [markdown]
# # Notes 
# 1. Outer join: All the indices appear. 
# 2. Inner join: The indices I0 and I1 appear (No NaNs).
# 3. Left join: The indices I0, I1 and I2 appear. 
# 4. Right join: The indices I0, I2 and I3 appear. 
# 5. Just one thing to note about join is how its syntax is different from the merge.



# %% [markdown]
# # More pandas functions 
# %% [code]
# Have a look at the dfs
df8
df9
# Finding unique values in a column/series
df8['color'].unique()
# Finding the counts of unique values
df8['color'].value_counts()
# Finding mean of cols
df9.mean()
# Getting the list of all cols 
df8.columns



# %% [markdown]
# # Notes 
# 1. Observe that the result of `value_counts()` is a series with indices as the color names and their counts as int.
# 2. But, the output of `unique()` function is a numpy array



# %% [markdown]
# # Creating a new dataframe using logical indexing
# %% [code]
# Create a logical/boolean series
(df8['customer2']!='105') & (df8['color']!='yellow')
# Create df using the above boolean series
new_df = df8[(df8['customer2']!='105') & (df8['color']!='yellow')]
new_df



# %% [markdown]
# # Apply inbuilt functions 
# %% [code]
print(df8['sales'].sum())
print(df8['distance'].min())



# %% [markdown]
# # Apply a user defined function over a series
# %% [code]
# Define custom function
def profit(s):
    return s*0.5 
# Apply
df8['sales'].apply(profit)



# %% [markdown]
# # Apply other inbuilt functions not built for pandas
# %% [code]
# len cannot be directly applied over a series like series.len
df8['color'].apply(len)



# %% [markdown]
# # `apply()` and `applymap()` over a df - e.g. 1
# %% [code]
# apply()
df11 = df8[['distance','sales']]
df11.apply(profit)
# applymap()
df11.applymap(profit)



# %% [markdown]
# # Notes 
# 1. `apply()` can be used over a df or a series. When used over a df it works series by series i.e., it takes into input one series returns a result and moves to next series.
# 2. `apply(profit)` takes into input the series `distance` and applies the function `profit()` over that series. This returns the half of as many values as there are in that series. It then takes into input the next series i.e., `sales` and applies the same function over that series. 
# 3. On the other hand, `applymap()` only works over a dataframe, works entry by entry of the dataframe, and always returns back the entire dataframe. 
# 4. `applymap(profit)` takes the input of each value in the df and returns the half of each value.
# 5. The results of both the above are same here but the manner in which operations are done is very important.



# %% [markdown]
# # `apply()` and `applymap()` over a df - e.g. 2
# %% [code]
# Define a function
def col_sum(co):
    return sum(co)
# apply()
df11.apply(col_sum) 
# applymap()
# df11.applymap(col_sum)  # will return error


# %% [markdown]
# # Notes
# 1. `df.applymap()` here throws an error its because the function (`col_sum()`) argument takes in a series and if we apply it to an individual entry we are going to get an error.



# %% [markdown]
# # Deleting cols from a df
# %% [code]
del df8['color']  # no `inplace` required
df8



# %% [markdown]
# # Looking at index values of a df
# %% [code]
df8.index



# %% [markdown]
# # Sorting values in a df
# %% [code]
df8.sort_values(by='distance',inplace=True)
df8



# %% [markdown]
# # Grouping rows in a col
# If some series has multiple values then we can group all the unique values of that series together 
# %% [code]
# Firstly define a dataframe
mydict = {'customer': ['Customer1','Customer1','Customer2','Customer2','Customer3','Customer3'], 'product1': [1.1,2.1,3.8,4.2,5.5,6.9], 'product2': [8.2,9.1,11.1,5.2,44.66,983]}
df6 = pd.DataFrame(mydict,index=['Purchase 1','Purchase 2','Purchase 3','Purchase 4','Purchase 5','Purchase 6'])
df6



# %% [markdown]
# # Group same rows in col customer
# %% [code]
grouped_data = df6.groupby('customer')
print(grouped_data)



# %% [markdown]
# # Find all stats of the grouped values
# %% [code]
grouped_data.describe()
grouped_data.mean()



# %% [markdown]
# # Notes 
# 1. `grouped_data.describe()` results in a pivot table where the mean of the rows with same values under the col `customer`, are calculated for the rest of the cols of the df. Other descriptors such as count, std dev, etc. are also given.
# 2. `grouped_data.mean()` is showing only mean for the rest of the cols of the df.



# %% [markdown]
# # Saving dataframes to csv
# %% [code]
df8.to_csv('../02_OutFiles/df8.csv', index=True)



# %% [markdown]
# # Notes
# 1. Here `to_csv()` is a method of the object df8 in the class dataframe.
# 2. We have explcitly specified to save the index of df8 while saving it. The other option would be `index=False` and the data from the first col i.e., `customer` would have been saved into the csv.



# %% [markdown]
# #  Loading the saved dataframes
# %% [code]
# index_col=0
new_df8 = pd.read_csv('../02_OutFiles/df8.csv', index_col=0)
new_df8
# index_col not specified
new_df8 = pd.read_csv('../02_OutFiles/df8.csv')
new_df8
# index_col=0
new_df8 = pd.read_csv('../02_OutFiles/df8.csv', index_col=1)
new_df8



# %% [markdown]
# # Notes
# 1. `index_col=0` tells python to consider the first col of csv file as the index
# 2. not specifying anything results in reading this index col with no header as a data col. Python will give it a label 'Unnamed: 0'. 
# 3. `index_col=1` tells python to take the second col of the csv file as the index. The first col will be read as a data col under the label 'Unnamed: 0'.



# %% [markdown]
# # Saving and loading df in Excel files
# %% [code]
# Saving to excel
df8.to_excel('../02_OutFiles/df8.xlsx',index=False,sheet_name='first sheet')
# index_col=0
newer_df8 = pd.read_excel('../02_OutFiles/df8.xlsx',sheet_name='first sheet',index_col=0)
newer_df8
# index_col not specified
newer_df8 = pd.read_excel('../02_OutFiles/df8.xlsx',sheet_name='first sheet')
newer_df8
# index_col=1
newer_df8 = pd.read_excel('../02_OutFiles/df8.xlsx',sheet_name='first sheet',index_col=1)
newer_df8



# %% [markdown]
# # Notes 
# 1. `to_excel()` is a method inside the `df8` object of the class dataframe. 



# %% [markdown]
# # That's all folks!



# %%