# %% [markdown]
# # About 
# This code is a case study available on kaggle (aimed at illustrating statistics)
# ### Case study - Stack Overlfow Annual Developer Survey results
# 
# ### Agenda of this Case Study:
# Derive insights from the data, in doing so we will learn to use python to fetch, manipulate, see and understand data, and, get familiar with some common python libraries and functions we use for EDA
# 
# ### Context of the dataset we are going to use:
# Each year, we at Stack Overflow ask the developer community about everything from their favorite technologies to their job preferences. This year marks the eighth year we’ve published our Annual Developer Survey results—with the largest number of respondents yet. Over 100,000 developers took the 30-minute survey in January 2018.
# 
# This year, we covered a few new topics ranging from artificial intelligence to ethics in coding. We also found that underrepresented groups in tech responded to our survey at even lower rates than we would expect from their participation in the workforce. Want to dive into the results yourself and see what you can learn about salaries or machine learning or diversity in tech? We look forward to seeing what you find!
#
# ### Content:
# This 2018 Developer Survey results are organized on Kaggle in two tables:
# 
# `survey_results_public` contains the main survey results, one respondent per row and one column per question
# 
# `survey_results_schema` contains each column name from the main results along with the question text corresponding to that column
#
# There are 98,855 responses in this public data release. These responses are what we consider “qualified” for analytical purposes based on completion and time spent on the survey and included at least one non-PII question. Approximately 20,000 responses were started but not included here because respondents did not answer enough questions, or only answered questions with personally identifying information. Of the qualified responses, 67,441 completed the entire survey.



# %% [markdown]
# # Libraries
# %% 
%matplotlib inline
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# %% [markdown]
# # Read dataset
# if the dataset `survey_results_public.csv` is not available in the input files 
# then it can be downloaded easily from the kaggle page: https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2018-developer-survey?select=survey_results_public.csv
# %% 
df = pd.read_csv('../01_InFiles/survey_results_public.csv')
questions = pd.read_csv('../01_InFiles/survey_results_schema.csv')



# %% 
print(df.shape)
df.head() 



# %% [markdown]
# # Notes
# - We got an error above, stating that there is a mix of data types in certain columns
# - From the data above we can see that the column 'Company Size' has numbers and strings 
# - Similarly it is the case for certain other columns
# - The warning message says either specify the dtype of each and every column or set low_memory = False. The latter is more feasible for this dataset having 129 columns



# %% [markdown] 
# # Correcting warning in reading dataset
# %% 
df = pd.read_csv('../01_InFiles/survey_results_public.csv', low_memory = False)  



# %% [markdown]
# # Notes
# - Most warnings are often harmless but it is necessary to be cognizant of the same
# - The way to deal with these warnings is often documented in the library that we use
 


# %% [markdown]
# # Explore *survey schema data*
# %% 
questions.head(20) 



# %% [markdown]
# # Notes
# - We can see how the table is structured
# - Each column in df is essentially a question and the column name is an alias for that question
# - We can see any question in its entirety by fetching it from the questions dataframe



# %% [markdown]
# # Fetch a question's text
# %% 
questions.loc[4,'QuestionText']  



# %% [markdown]
# # Notes
# - We used `.loc[ ]` to fetch a specific value from the dataframe
# - But what if we did not know the position of a certain column name whose question we want to fetch?



# %% [markdown]
# # Using question alias to fetch the text
# Set question alias as the index so that we can use the questions' alias to fetch 
# the text using through the `.loc[]` 
# %% 
questions.set_index('Column', inplace=True)
questions.head()
# %% 
# Example fetch
questions.loc['Student', 'QuestionText']



# %% [markdown]
# # Basic info of the df
# %% 
df.info()



# %% [markdown]
# # Notes
# - Of the 129 columns, 41 are float type, 1 is integer type and the rest 87 are object type data
# - We have 98855 rows in total
# - And the amount of memory this dataset is occupying on the RAM is 97.3MB



# %% [markdown]
# # Count the number of NaNs
# %% 
df.isna()
# %% 
df.isna().apply(pd.value_counts)



# %% [markdown]
# # Notes
# - Treating missing values is beyond the scope of this notebook, hence we will ignore it for now



# %% [markdown]
# # Top countries according to userbase
# %% 
# Listing all columns 
np.array(df.columns)
# %% 
# Get top 10 countries according to userbase
df.Country.value_counts().head(10)
# %% 
# Barplot of above stats for top 25 countries
df.Country.value_counts().head(25).plot(kind = 'bar', edgecolor = 'black', color = 'lightblue', figsize = (15,5))
plt.xlabel('Country')
plt.ylabel('Number of users')
plt.title('Top 25 countries in terms of userbase')
plt.show()



# %% [markdown]
# # Selecting only the rows of top 25 countries
# %% 
# List of top 25 countries
df.Country.value_counts().head(25).index
# %%
# Checking for each entry of the df if its in the above list
df.Country.isin(df.Country.value_counts().head(25).index)
# %%
# Using logical indexing to get the df rows with only 'True' i.e. the rows which correspond to the countries in the top 25 countries list
df.loc[df.Country.isin(df.Country.value_counts().head(25).index), :]
# %%
# Store this info in a variable
top25 = df.loc[df.Country.isin(df.Country.value_counts().head(25).index), :]



# %% [markdown]
# # Plot 
# %% 
# See what `pd.crosstab` shows
# %% 
# Generate the plot for the count of 'open-source' and 'not open-source' for all the top 25 countries
pd.crosstab(top25.Country, top25.OpenSource).plot(kind = 'bar', edgecolor = 'black', color = ['lightblue', 'lightgreen'], figsize = (15,5))
plt.xlabel('Country')
plt.ylabel('Number of users')
plt.title('Top 25 countries in terms of userbase, segregated by their contribution to open source projects')
plt.show()



# %% [markdown]
# # Notes
# - The green bars indicate the population that contributes to open source projects and the blue indicates the rest
# - If we want to the bars to be sorted the same way as the earlier plot, we can index the crosstabdata in that order



# %% [markdown]
# # Sort the above plot in the same way as the earlier plot
# %% 
# The list to be used for sorting the pd.crosstab entries 
df.Country.value_counts().head(25).index
# %%
# Plot
pd.crosstab(top25.Country, top25.OpenSource).loc[df.Country.value_counts().head(25).index,:].plot(kind = 'bar', edgecolor = 'black', color = ['cyan', 'green'], figsize = (15,5))
# Labels and title
plt.xlabel('Country')
plt.ylabel('Number of users')
plt.title('Top 25 countries in terms of userbase, segregated by their contribution to open source projects')
plt.show()



# %% [markdown]
# # Notes
# - Proportionally, Indian users seem to be contributing more for open source projects than most other countries
# - In case of Turky, the two categories are almost the same
# - In case of Iran, the open source contributors are more compared to the ones that don't.



# %% [markdown]
# # Task 
# Write a piece of code to plot the number of users who code as a hobby vs number of users who do not, by country (consider the top 10 countries in terms of user base).



# %%
# Get the top 10 countries
top10 = df.loc[df.Country.isin(df.Country.value_counts().head(10).index), :]
# %% 
# Country wise coders count (hobby vs non hobby)
pd.crosstab(top10.Country, top10.OpenSource)
# %% 
# Plot (in the same order of countries as previous plots)
# As used previously, `loc[df.Country.value_counts().head(10).index,:]` will be used to order the countries 
pd.crosstab(top10.Country, top10.OpenSource).loc[df.Country.value_counts().head(10).index,:].plot(kind = 'bar', edgecolor = 'black', color = ['cyan', 'green'], figsize = (15,5))
# Labels and title
plt.xlabel('Country')
plt.ylabel('Number of users')
plt.title("Top 10 countries in terms of userbase, segregated by developers who code as hobby vs those who don't")
plt.show()



# %% [markdown]
# # Exploring the jobs of Devs
# %% 
df.DevType.unique()


# %% [markdown]
# # Notes
# - A lot of entries/developers have composite job titles
# - We have to write some additional steps to seperate the titles



# %% [markdown]
# # Seperate the Devs' job titles - error
# %% 
# df.DevType.apply(lambda x: x.split(sep = ';'))



# %% [markdown]
# # Notes
# - The reason for the above error (`AttributeError: 'float' object has no attribute 'split'`) is the presence of NaN values in the data
# - We can avoid it by using `try and except` block



# %% [markdown]
# # Seperate the Devs' job titles
# %% 
# Define the the function to handle the error/exception
def split_title(title):
    try:
        return title.split(sep = ';')
    except:
        return []
# %% 
# Seperate the job titles
titles = df.DevType.apply(lambda x: split_title(x))
titles.head()



# %% [markdown]
# # Notes
# - What we are getting in the above code is a series of lists
# - The next step would be to combine these lists



# %% 
title_list = []
for composite_title in df.DevType:
    title_list.extend(split_title(composite_title))
# %% 
len(np.unique(title_list))



# %% [markdown]
# # Notes
# - The above list contains all the job titles of the user base
# - There are 20 unique job titles in the user pool
# - Beyond just the job titles we can also get the count of individual job titles and see the proportion of each job title in the user pool



# %% 
# Get frequency of each job title
series = pd.Series(title_list).value_counts()
series
# %% 
# Modify the 'explode' parameter to highlight the job titles of data science people
explode = np.zeros(len(series))
print('explode=', explode,'\n')
indices = series.index.isin(['Data or business analyst', 'Data scientist or machine learning specialist'])
print('indices=', indices,'\n')
explode[indices] = 0.1
print("modified 'explode'=", explode,'\n')
# %% 
# Plot the pie chart (using the above 'explode')
plt.figure(figsize=(15,15), facecolor='lightgrey');
plt.pie(series, labels = series.index, autopct='%.1f%%',shadow = True, explode = explode, textprops={'fontsize': 14});
plt.show()



# %% [markdown]
# # Notes
# - The proportion of users who are in analytics or ML field are about 5.3%
# - Close to 50% of the cohort are web developers
# 
# **code explanation**: We got the frequency of job titles from title_list, by converting it to series and using the pd.value_counts method. Using these frequency counts, we made a pie chart. To pop the two specific job titles, we got a boolean array of series where the value is equal to the specific job title. We used this boolean array to index an array of zeros and replace the values in the array with a non-zero number



# %% [markdown]
# # Let's look only at analysts : Plot the age groups of analysts
# %% 
# Boolean array of analysts
df.DevType.isin(['Data or business analyst', 'Data scientist or machine learning specialist'])
# %% 
# Filter out the analysts from the main df
analysts = df.loc[df.DevType.isin(['Data or business analyst', 'Data scientist or machine learning specialist']), :]
analysts.head(10)
# %% 
analysts.shape
# %%
# Look at the `Age` col of the `analyts` df
analysts.Age.value_counts()
# %%
# Get the frequency of each age group
analysts.Age.value_counts()
# %% 
# Plot 
analysts.Age.value_counts().plot.barh().invert_yaxis()



# %% [markdown]
# # Notes
# - A significant majority of the data science professionals are of the age group 25-34



# %% [markdown]
# Plot the satisfaction level of each age group in the above
# %%
# Satisfaction level for each age group
pd.crosstab(analysts.JobSatisfaction, analysts.Age)
# %%
# Satisfaction level for each age group with normalized values
pd.crosstab(analysts.JobSatisfaction, analysts.Age, normalize = 'columns')
# %% 
# Plot 
plt.figure(figsize=(9,5))
sns.heatmap(pd.crosstab(analysts.JobSatisfaction, analysts.Age, normalize = 'columns'), cmap = 'Blues', annot = True)
plt.show()



# %% [markdown]
# # Notes 
# - 67% of the majority age-group i.e, 18-24, are quiet satisfied with their jobs
# - Age groups 45-54 and 55-64 seem to be dissatisfied with their data science jobs



# %% [markdown]
# # Monthly salaries of the analysts
# %% 
# Filter out the relevant salary cols from the df
salaries = analysts.loc[:,['Salary', 'SalaryType', 'Currency', 'ConvertedSalary']].dropna()
# Remove the commas from the 'Salary' col
salaries['Salary'] = salaries.Salary.apply(lambda x: x.replace(',', '')).apply(float)
salaries.head(10)
# %% 
# Frequency of different salary types 
salaries.SalaryType.value_counts()
# %% 
# Convert all salaries to monthly salary
# Firstly add a new col 
salaries['monthly_salary'] = salaries.ConvertedSalary
# Then convert the yearly and weekly ones to monthly scale
for i in salaries.index:
    if salaries.loc[i, 'SalaryType'] == 'Yearly':
        salaries.loc[i, 'monthly_salary'] = salaries.loc[i, 'ConvertedSalary']/12
    elif salaries.loc[i, 'SalaryType'] == 'Weekly':
        salaries.loc[i, 'monthly_salary'] = salaries.loc[i, 'ConvertedSalary']*4
# %% 
salaries.head()
# %% 
# Plot
fig, ax = plt.subplots(1,2, sharex = True)
fig.set_figheight(5)
fig.set_figwidth(20)
sns.boxplot(salaries.monthly_salary, ax= ax[0])
sns.distplot(salaries.monthly_salary, ax = ax[1])
plt.show()



# %% [markdown]
# # Notes 
# - Histogram in this case does not give much information because of the extreme skew in the distribution
# - The data is highly skewed. Hence, we will look at the numbers



# %% [markdown] 
# # Look at the salary numbers
# %% 
salaries.monthly_salary.describe().apply(lambda x: format(x, '.2f'))



# %% [markdown]
# # Notes
# - 75% of the people have salaries less than 19140 USD and the median salary for a data scientist is 7750 USD



# %% [markdown]
# # Indian salaries
# %% 
# Boolean array of Salaries in Indian currency
salaries.Currency.apply(lambda x: 'Indian' in x)
# %% 
# Select the salaries in Indian currency, from the df
Indian_salaries = salaries.loc[salaries.Currency.apply(lambda x: 'Indian' in x), :]
# %% 
# Get all kinds of salaries into monthly format
Indian_salaries['monthly_salary'] = Indian_salaries.Salary
for i in Indian_salaries.index:
    if Indian_salaries.loc[i, 'SalaryType'] == 'Yearly':
        Indian_salaries.loc[i, 'monthly_salary'] = Indian_salaries.loc[i, 'Salary']/12
    elif Indian_salaries.loc[i, 'SalaryType'] == 'Weekly':
        Indian_salaries.loc[i, 'monthly_salary'] = Indian_salaries.loc[i, 'Salary']*4
# %% 
# top 5 monthly Indian salaries
pd.set_option('display.float_format', lambda x: '%.3f' % x)
Indian_salaries.sort_values(by='monthly_salary', ascending=False).head(20)
# %% 
# Plot
fig, ax = plt.subplots(1,2, sharex = True)
fig.set_figheight(5)
fig.set_figwidth(20)
sns.boxplot(Indian_salaries.monthly_salary, ax= ax[0])
sns.distplot(Indian_salaries.monthly_salary, ax = ax[1])
plt.show()



# %% [markdown] 
# # Look at the salary numbers
# %% 
Indian_salaries.monthly_salary.describe().apply(lambda x: format(x, '.0f'))



# %% [markdown]
# # Notes
# - From the above numbers and plots we can see that the median salary for a professional in data science or business analytics field in India is about 58k per month
# - However the max value shows that it is 2Cr, which is a not a reasonable number 
# - These unreasonable numbers are called outliers
# - We will learn about outliers and how to deal with them in later modules



# %% [markdown]
# # Conclusion:
# Now that we got a good idea of how to plot, manipulate, draw insights and extract relevant data from a huge dataset, and we still have a lot of unexplored columns in the dataset!
# 
# All the best!   


