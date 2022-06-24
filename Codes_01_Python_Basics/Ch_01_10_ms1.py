# %% [markdown]
# # About
# This code is a public case study available on kaggle - to illusrate python basics (numpy and pandas).
# ## Case study  - Uber Data Analysis
# The data of a driver’s uber trips are available for year 2016. The manager wants us to explore this data to give him <u>some useful insights</u> about the trip behaviour of the Uber driver.
# ## About dataset
# The dataset contains Start Date, End Date, Start Location, End Location, Miles Driven and Purpose of drive (Business, Personal, Meals, Errands, Meetings, Customer Support etc.)
# ## Concepts covered:
# 1. Data profiling
# 2. `.groupby()` function
# 3. `.apply()` function 
# 4. DateTime operations 



# %% [markdown]
# # Libraries
# %% [code]
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import calendar
start = pd.Timestamp.now()  



# %% [markdown]
# # Read data
# %% [code]
# Firstly lets explore pandas features of reading data from hdd
# Skip first n nows 
df = pd.read_csv('../01_InFiles/Uber+Drives+2016.csv', skiprows = 100)  
df
# Load only the first n rows
df = pd.read_csv('../01_InFiles/Uber+Drives+2016.csv', nrows = 100)  # 
df
# Load only selected columns
df = pd.read_csv('../01_InFiles/Uber+Drives+2016.csv', usecols = ['START_DATE*', 'END_DATE*'])  
df
# Finally read data as required
df = pd.read_csv('../01_InFiles/Uber+Drives+2016.csv')
df



# %% [markdown]
# # Beautiful report from Pandas profiling [optional](optional)
# %% [code]
# # Regular report
# profile = ProfileReport(df, title="Pandas Profiling Report")
# profile.to_widgets()  # style 1
# profile.to_notebook_iframe()  # style 2
# # Explorative report
# profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
# profile.to_notebook_iframe()
# # Minimal report
# profile = ProfileReport(df, minimal=True)
# # Save if req
# profile.to_file("../02_OutFiles/pandasProfiling.html")



# %% [markdown]
# # Notes 
# 1. Whether we apply `.to_widgets()` or `.to_notebook_frame()` the profile style is same when saved into an html.



# %% [markdown]
# # Rename columns for readability
# %% [code]
# Form a new list and modify col names
col_names = ['START_DATE','END_DATE','CAT', 'START' , 'STOP' , 'MILES','PURPOSE']
df.columns = col_names
# OR by using `.replace()` in case of large no. of cols
# df.columns = df.columns.str.replace("*", "")  
# OR by renaming specific cols
# df.rename( columns = {'CAT':'CATEGORY'})
df.head()



# %% [markdown]
# # Understand data
# %% [code]
df.head(8) 
df.tail(10)
print(df.shape)
# Overall view
df.info()
df.count()  # same as above, gives non-null number of records



# %% [markdown]
# # Notes
# 1. It appears that there are a total of 1156 rows. The columns having 1155 non-null rows have one NaN due the last 'Totals' row. 
# 2. `PURPOSE` column has lots of missing values  



# %% [markdown]
# # Explore NaNs 
# %% [code]
# NaNs per column 
df.isnull().sum()
# NaNs per column - logical output 
df.isnull().any() 
# NaNs in entire df - logical output
df.isnull().any().any()
# Get the list of columns having any NaNs
null_cols = df.columns[df.isnull().any()]
list(null_cols)



# %% [markdown]
# # Explore `PURPOSE` column
# %% [code]
# Entries where PURPOSE is null
df[df['PURPOSE'].isnull()].head()    
# Entries where PURPOSE is not null
df[~df['PURPOSE'].isnull()].head()
# Count of non-nulls in this col
df['PURPOSE'].count()



# %% [markdown]
# # SQL Like queries
# SQL like queris can also be made on any col
# %% [code]
# Get records with MILES>30
df[df['MILES'] > 30]
df[df.MILES == 30]
df[df.MILES != 30]
# Same query in SQL format
df.query('MILES > 30')




# %% [markdown]
# # Explore `MILES` column
# %% [code]
# Top ten rows of max and min MILES
df.sort_values(by = 'MILES' , ascending = False).head(10) 
df.sort_values(by = 'MILES' , ascending = True).head(10) 
# At this point - see Notes
# Remove the row c/t anomalously high MILES value
df[df.MILES ==df.MILES.max()]  
df = df[df.MILES < 1000]  



# %% [markdown]
# # Notes 
# 1. On investigating the ten highest and lowest values in `MILES` col, the max `MILES` value looked suspicious going much beyond the range of the rest of the values i.e., 0.5 to 310.3.
# 2. This led us to the decision of removing the suspicious value.



# %% [markdown]
# # Explore numerical cols of df
# %% [code]
df.dtypes
df.describe().T



# %% [markdown]
# # Drop rows with null values
# %% [code]
df_dropped = df.dropna()  
df_dropped.shape
df.shape



# %% [markdown]
# # Notes 
# 1. Don't drop rows from the original dataframe as we'd lose good rows with values, so always make a copy
# 2. The values were dropped because almost half of the values cannot be interpolated without the opinion of subject matter expert (1155-653=502)



# %% [markdown]
# # Explore the data parameter wise: 
# 1. Destination - (starting and stopping)
# 2. Time - (hour of the day, day of week, month of year)
# 3. Categories
# 4. Purpose 
# 5. Grouping two parameters to get more insights



# %% [markdown]
# # Destination - Unique points
# %% [code]
# Get unique starting points
df['START'].unique()
len(df['START'].unique())  # count using len
df['START'].nunique()  # count using nunique() 
# Get unique stopping points
df['STOP'].unique()
len(df['STOP'].unique())



# %% [markdown]
# # Set operations example
# %% [code]
l1 = [1,2,3,4,4]
l2 = [3,4,5,6]
set(l2) - set(l1) # difference  
set(l1) - set(l2) # difference 
set(l2) | set(l1) # union 
set(l2) & set(l1) # intersection 



# %% [markdown]
# # Destination - Set operations
# %% [code]
# Set operations ease the comparison b/w two series/lists 
startSet  = set(df['START'])  # names of unique start points
stopSet =  set(df['STOP'])  # names of unique start points
print(len(startSet))
print(len(stopSet))
# Stations which appear in both start and stop locations 
stopSet & startSet
len(stopSet & startSet)



# %% [markdown]
# # Destination - Identify popular stations
# %% [code]
# Popular starting stations - top 10
df['START'].value_counts().head(10)
# Popular stopping stations - top 10
df['STOP'].value_counts().head(10)
# Rount trip stations
df[df['START'] == df['STOP']]



# %% [markdown]
# # Destination - Favourite starting point w.r.t. miles covered
# %% [code]
k = df.groupby('START')['MILES'].sum().sort_values(ascending=False).head(10) 
k = k.reset_index()  # series to df
k.columns = ['START' ,'sum_of_miles']
sns.barplot(data=k , x='START' , y='sum_of_miles');
plt.xticks(rotation=70);



# %% [markdown]
# # Destination - Farthest start-stop pair w.r.t miles covered ever
# %% [code]
# Perform on subset df to understand what will happen
dfTest = df.head(10).copy(deep=True)
dfTest
dfTest.groupby(['START','STOP'])['MILES'].sum().sort_values(ascending=False)
# Perform on original df
df.groupby(['START','STOP'])['MILES'].sum().sort_values(ascending=False).head(10)



# %% [markdown]
# # Further, drop unknown location stations
# %% [code]
# Using start and stop conditions one by one
df2 = df[df['START']!= 'Unknown Location']
df2 = df2[df2['STOP']!= 'Unknown Location']
# OR 
# Using both conditions together
# df2 = df[(df.START != 'Unknown Location') & (df.STOP != 'Unknown Location')]
df2.groupby(['START','STOP'])['MILES'].sum().sort_values(ascending=False).head(10)



# %% [markdown]
# # Notes 
# 1. The start-stop pair with the max no. of miles covered ever is Morrisville-Cary followed closely by Cary-Durham and Cary-Morrisville



# %% [markdown]
# # Destination - most popular start-stop pair w.r.t. travel count
# %% [code]
# Perform on subset df to understand what will happen
dfTest1 = df2.head(10).copy(deep=True)
dfTest1
dfTest1.groupby(['START','STOP'])['MILES'].size().sort_values(ascending=False)
# Pefrom on real df
df2.groupby(['START','STOP'])['MILES'].size().sort_values(ascending=False).head(10)



# %% [markdown]
# # Notes
# 1. The most popular start-stop pair is Morrisville to Cary



# %% [markdown]
# # Time - convert format  
# %% [code]
df.head()
df.dtypes
# Convert start and end date into datatime format
df['start_dt'] = df['START_DATE'].apply(lambda x : datetime.strptime(x, '%m/%d/%Y %H:%M'))
df['end_dt'] = df['END_DATE'].apply(lambda x : datetime.strptime(x, '%m/%d/%Y %H:%M'))
df.head()
# See how the dtype is different now
df.dtypes  



# %% [markdown]
# # Time - explore the inbuilt functionalities of datatime module
# %% [code]
# Create more cols from timestamps
df['start_day'] = df['start_dt'].dt.day
df['start_hour'] = df['start_dt'].dt.hour
df['start_month'] = df['start_dt'].dt.month
# Also day of week - days encoded as 0-6 (Mon=0, Tue =1, etc.)
df['d_of_wk'] = df['start_dt'].dt.dayofweek   
df.head()



# %% [markdown]
# # Time - Convert week days from numeric form to text 
# %% [code]
# Using a dict and `.apply()` function
labels = {0:'Mon',1:'Tue',2:'Wed',3:'Thur',4:'Fri',5:'Sat',6:'Sun'}
df['day_of_week'] = df['d_of_wk'].apply(lambda x: labels[x])
df.head()
# OR
# Using the builtin functions 
df['day_of_week1'] = df['start_dt'].apply(lambda x : datetime.strftime(x,'%a'))  
df.head()



# %% [markdown]
# # Time - Convert month from numeric form to text
# %% [code]
df['cal_month'] = df['start_month'].apply(lambda x: calendar.month_abbr[x])
df.head()
# OR
# Use the built in functions in datatime module
df['cal_month1'] =  df['start_dt'].apply(lambda x : datetime.strftime(x,'%b'))
df.head()



# %% [markdown]
# # Time - Monthly stats
# %% [code]
# Which month did he get most drives ? 
df.groupby(['start_month']).size() 
# What are the total miles run each month ?
# Peform on test subset to understand what will happen
dfTest2 = df.iloc[55:65]
dfTest2
dfTest2.groupby('cal_month')['MILES'].sum().sort_values(ascending = False)
# Perform on real df 
df.groupby('cal_month')['MILES'].sum().sort_values(ascending = False)
# Similarly, find avg. dist. covered each month
df.groupby('cal_month').mean()['MILES'].sort_values(ascending = False)



# %% [markdown]
# # Time - daily and hourly stats
# %% [code]
#Which day did he get most drives  ? 
df.groupby(['day_of_week']).size()  
# Does he have a prefered time of start ?
dfTemp = df.groupby('start_hour').size()
dfTemp = dfTemp.reset_index()
dfTemp.columns = ['start_hour' ,'count']
sns.barplot(data= dfTemp , x ='start_hour' , y = 'count')



# %% [markdown]
# # Notes
# 1. Looks like he mostly starts the trip around 9-10 and the peak hours seem to be between 12-6 PM 



# %% [markdown]
# # Time - duration stats
# %% [code]
# Duration of the trips 
df['diff'] = (df['end_dt'] - df['start_dt'])
df.head()
# This creates a timedelta datatype
df.dtypes
# Convert to hour
df['diff_hr'] = df['diff'].astype('timedelta64[h]')
df['diff_hr'].describe()
# Further, convert to mins for easy inferencing
df['diff_mins'] = df['diff'].astype('timedelta64[m]')
df['diff_mins'].describe()



# %% [markdown]
# # Notes
# 1. There seems to be something strange with the minumum time (mins) - it is 0 that implies start and stop time are same



# %% [markdown]
# # Investigating more Time
# %% [code]
# Which rows have same start and stop time
len(df[df['START_DATE'] == df['END_DATE']])
df[df['START_DATE'] == df['END_DATE']]
# OR 
print(len(df))
# Remove such rows 
# By simply negating the above condition
df3 = df[~(df['START_DATE'] == df['END_DATE'])]
# OR
# By using new condition with !=
# df3 = df[df.start_dt != df.end_dt]
print(len(df3))



# %% [markdown]
# # Time - trip speeds
# %% [code]
# Trip speed for each trip
df3.head()
df3['Duration_hours'] = df3['diff_mins']/60
df3.head()
df3['Speed'] = df3['MILES']/df3['Duration_hours']
df3.head()
df3['Speed'].describe()
# At this point see Notes below
# Top 5 small duration trips
df3.sort_values(by ='diff_mins', ascending = True).head(5)
df3 = df3[(df3.diff_mins > 5)]  # trips that lasted atleast 5 mins 
# Top 5 small duration trips now
df3.sort_values(by ='diff_mins', ascending = True).head(5)



# %% [markdown]
# # Notes 
# 1. There are some really speedy cars as seen in `df3['Speed'].describe()`. One +ble reason is the small value of denominator i.e. time.
# 2. We should remove such records by taking a cutoff of time duration as 5 mins as trips with lesser duration make no sense. This cutoff can vary though.



# %% [markdown]
# # Category & Purpose
# %% [code]
df['CAT'].value_counts()



# %% [markdown]
# # Notes
# 1. Most trips are in the business category



# %% [markdown]
# # Purpose
# %% [code]
df['PURPOSE'].value_counts()
# Average distance traveled for each activity
df.groupby('PURPOSE').mean()['MILES'].sort_values(ascending = False)



# %% [markdown]
# # Notes
# 1. Most trips are for meetings.



# %% [markdown]
# # Last questions - Question1
# Question 1: How many miles were covered per category and purpose ?
# %% [code]
# Answer1: 
# Per category
df.groupby('CAT').sum()['MILES'].sort_values(ascending = False)
# Per purpose
df.groupby('PURPOSE').sum()['MILES'].sort_values(ascending = False)



# %% [markdown]
# # Last questions - Question2
# Question 2: What is percentage of business miles vs personal?
# %% [code]
df4 = df.groupby('CAT').agg({'MILES':'sum'})
df4
df4.apply(lambda x: x/x.sum()*100).rename(columns = {'MILES':'% of Miles'})



# %% [markdown]
# # Notes 
# 1. @L:511 the `.agg()` function does the same as `.sum()`, but the former returns a df unlime the latter.



# %% [markdown]
# # Last questions - Question3
# Question 3: How much time was spend for drives per category and purpose?
# %% [code]
# Answer3:
# Per category
df4= df.groupby('CAT').sum()['diff_mins'].sort_values(ascending = False)
df4.apply(lambda x: x/60)
# Per purpose
df5= df.groupby('PURPOSE').sum()['diff_mins'].sort_values(ascending = False)
df5.apply(lambda x: x/60)
print('Time elapased:', (pd.Timestamp.now()-start).total_seconds())



# %% 