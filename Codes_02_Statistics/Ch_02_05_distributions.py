# %% [markdown]
# # **About:**
# This code covers the following concepts:
# - **Binomial Distribution**
# - **Continuous Uniform Distribution**
# - **Normal Distribution**




# %% [markdown]
# # **Binomial Distribution**
# # Problem statement 
# 80% of all the visitors to Lavista Museum end up buying souvenirs from the souvenir shop at the Museum. On the coming Sunday if a random sample of 20 visitors will be picked: 
# 1. Find the probability that every visitor will end up buying souvenirs. 
# 2. Find the probability that a maximum of 7 visitors will buy souvenirs from 
# the souvenir shop.
# %% [markdown]
# ## Interpretation 
# The interpretation that 80% of all visitors will buy is translated to 80% 
# chance that a single visitor will buy. 
# %% [markdown]
# ## Assumptions 
# 1. There are only two possible outcomes for a given trial (success or failure) i.e., a visitor will buy a souvenir or not. 
# 2. Number of trials is fixed - there are 10 repetitions or 10 visitors in the sample $(n=10)$. 
# 3. Each trial is independent of the other trials. 
# 4. The probability of success is the same for each trial $(p=0.8)$



# %% [markdown]
# # Libraries
# %%
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
# scipy library contains a large number of probability distributions, and continuously growing
import scipy.stats as stats  



# %% [markdown]
# # Let's estimate the probability distribution of visitors
# %%
# Declare the sample size - `n` representing the number of visitors selected randomly
n = 10
# Declare `p` which represents the probability of success (probability that a visitor will end up buying a souvenir or not)
p = 0.80
# Declare different possible number of successes
k = np.arange(0,11)
k



# %% [markdown]
# The probability function of Binomial Distribution provides the probability for  $x$  number of successes from $n$ trials where $p$ is the probability of success 
# >$P(X=x)= {n\choose x}p^x(1-p)^{n-x}$
# Here, we know that:
# * $n$ (number of visitors selected randomly) = 10
# * $p$ (probability of success i.e., the probability that a visitor will end up buying a souvenir) = 0.80
# * $q$ (probability of failure i.e., the probability that a visitor will not end up buying a souvenir) = 1 - 0.80 = 0.20
# * $x$ (number of successes) = 10 <br/>
# We will use `binom.pmf()` to calculate this probability function which provides the probability for the number of visitors (out of $n=10$) that will end up buying souvenirs from the souvenir shop.



# %% [markdown]
# # Generate the probability distribution
# %%
from scipy.stats import binom
binomial = binom.pmf(k=k, n=n, p=p)
binomial



# %% [markdown]
# # Notes
# 1. In the above output `binomial` is the array of probabilities for different number of successes.
# 2. For example the probability of having 0 success (or 0 person buys; k=0) is the first value of `binomial` array, the probability of having 1 success (k=1) is the second value of the `binomial` array.
# 3. The last element of this `binomial` array represents the probability when the number of successes is 10 (which means that all 10 visitors (out of 10 selected randomly) will buy souvenirs from the souvenir shop).



# %% [markdown]
# Plot the distribution
# %%
plt.bar(k, binomial) # make a bar plot
plt.title("Binomial: n=%i , p=%.2f" % (n, p), fontsize=15) # set the title
plt.xlabel("Number of Successes") # set the x-axis label
plt.ylabel("Probability of Successes") # set the y-axis label
plt.show() # display the plot



# %% [markdown]
# # Notes
# 1. If we expect 80% of the people to buy a souvenir then the chance that exactly 8 out of 10 do buy a souvneir is about 30% or 0.3.
# 2. The above is the distribution of 6 people buying, 7 people buying, 8 people buying, etc. laid out as a bar chart. 


# %% [markdown]  
# # Ans. 1
# if there is an 8 in 10 chance (80% chance) that every visitor buys a 
# souvenir, and exactly 10 people visit the museum,then there is about an 11% 
# chance that everybody will buy something from the souvenir shop. 



# %% [markdown]
# # Notes
# 1. For answering the second question, we need to calculate the probability for $P(X<=7)$ i.e, accumulated probability or CDF.
# 2. **CDF** of a Random variable (X) is the probability that $X$  will take the value less than or equal to $x$. It is used to calculate the cumulative probability, and can be represented mathematically as below.
# >$F_X(x) = P(X\leq x)$ <br/>
# 
# In our case, Random Variable $(X)$ is the number of visitors who will buy souvenirs from the souvenir shop and we need to find $P(X\leq 7)$.



# %% [markdown]
# # Ans. 2
# %%
barl = plt.bar(k, binomial) 
plt.title("Binomial: n=%i , p=%.2f" % (n, p), fontsize=15) # set the title
plt.xlabel("Number of Successes") # set the x-axis label
plt.ylabel("Probability of Successes") # set the y-axis label
for i in range(0, 8):
    barl[i].set_color("r") # color the bars where no. of successes < 8
plt.show() 



# %% [markdown]
# 1. In the above graph, the red region represents P(X<=7).
# 2. The sum of the probabilities of the red bars will give the probability of atleast 7 visitors buying from the souvenir shop = `binomial[:8].sum()` = 0.3222 or 32.22%.
# 3. This can also be calculated using the `cdf` function in the manner given 
# below.
# %%
binomial[:8].sum()
# %%
binom.cdf(k=7, n=n, p=p)



# %% [markdown]
# # Notes
# 1. One interpretation of **Ans. 2** is in an year of sundays and every sunday 10 people come in, then roughly about 1/3rd of the sundays, we will get roughly about 7 or fewer people buying souvenirs. 



# %% [markdown]
# # More usage of `cdf` function
# If we wish to know the probability of having 'atleast x' no. of success, then it can be calculated using P(X>=x) 1 - cdf(x) as demonstrated below.
# %% 
# Probability of having ateast 4 success
1 - binom.cdf(k=3, n=n, p=p)



# %% [markdown]
# # Change in distribution with `p`
# Let's try to change the probability of success (probability that each visitor will buy souvenirs from the souvenir shop) to different values like 60%,70%,90%,95% and visualize how the shape of the distribution changes.
# %%
# Probability distribution for p=0.7
binomial_70 = binom.pmf(k, n, p=0.7)
# Plot
plt.bar(k, binomial_70)
plt.title("p=%.2f" % (0.7), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
# %%
# Probability distribution for p=0.8
binomial_80 = binom.pmf(k, n, p=0.8)
# Plot
plt.bar(k, binomial_80)
plt.title("p=%.2f" % (0.8), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
# %%
# Probability distribution for p=0.9
binomial_90 = binom.pmf(k, n, p=0.9)
# Plot
plt.bar(k, binomial_90)
plt.title("p=%.2f" % (0.9), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
plt.tight_layout(w_pad=5)



# %% [markdown]
# # Conclusion
# 1. It is clear from the above plot that the shape of the distributions change as the value of $p$ (probability of success) changes.
# 2. Use **binomial distributon** in cases when there are lots of people or cases and only two things can happen, e.g. default or not, rain or not, 



# %% [markdown]
# 
# # <a name='link2'>**Continuous Uniform Distribution**</a>

# %% [markdown]
# ### Problem statement
# 
# 
#  IT industry records the amount of time a software engineer needs to fix a  bug in the initial phase of software development in 'debugging.csv'.
# 
# Let
# 
# X = Time needed to fix bugs
# 
# 
# X is a continuous random variable. Let's see the distribution of X and answer the below questions.
# 
# 
# 1. Find the probability that a randomly selected software debugging requires less than three hours
# 
# 2. Find the probability that a randomly selected software debugging requires more than two hours
# 
# 3. Find the 50th percentile of the software debugging time
# 

# %% [markdown]
# 
# ### Reading the Data into the Dataframe

# %%
debugging = pd.read_csv("debugging.csv")
debugging.head()

# %% [markdown]
# Let's plot the histogram of data along with the PDF of uniform distribution using the parameters minimum time required and maximum time required for bug fixing.

# %%
# visualize the distribution of the time needed for bug fixing
plt.hist(debugging["Time Taken to fix the bug"], density=True)
plt.axhline(1 / 4, color="red")
plt.xlabel("Time required for bug fixing")
plt.ylabel("Probability")
plt.title("Data Distribution")
plt.show()

# %% [markdown]
# Another way to recognize a uniform distribution in your data is to look at a density plot. We will use displot of seaborn library to visualize the distribution of time needed for bug fixing.

# %%
# Density plot of time taken to fix the bug
sns.displot(debugging["Time Taken to fix the bug"], kde=True)
plt.show()

# %% [markdown]
# **Insight**: As you can see from the above plot that all the values between 1 and 5 are having almost equal probability, we are going to use continuous uniform distribution. We need to decide the endpoints. Here, endpoints are 1 and 5.
# 
# X ~ U(1, 5)

# %%
# import the required function
from scipy.stats import uniform

# use the uniform.pmf() function to generate the probability distribution
x = np.linspace(1, 5, 50)
probs = uniform.pdf(x, loc=1, scale=4)

# %% [markdown]
# **Find the probability that a randomly selected software debugging requires a maximum time of 3 hours** 
# 
# **CDF:** of a random variable (X) is the probability that X  will take the value less than or equal to x. It can be represented mathematically as below.
# 
# >$F_X(x) = P(X\leq x)$
# 
# 
# In our case, random variable (X) is the number of hours.
# 
# $ P(X\leq 3)$

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
x1 = np.linspace(1, 3, 25)
plt.plot(x, probs)
plt.fill_between(x, probs)
plt.fill_between(x1, uniform.pdf(x=x1, loc=1, scale=4), color="r")
plt.xlabel("Time required for bug fixing")
plt.ylabel("Probability")
plt.title("Continuous Uniform Distribution: X ~ U(1,5)")
plt.show()

# %% [markdown]
# In the above graph, the red region represents P(X<=3). Let's calculate the probability that that a randomly selected software debugging requires a maximum time of 3 hours. We will use uniform.cdf() for this.

# %%
uniform.cdf(x=3, loc=1, scale=4)

# %% [markdown]
# 
# **Find the probability that a randomly selected software bug fixing requires more than two hours.**
# 
# $ P(X>2)$

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
x1 = np.linspace(2, 5, 20)
plt.plot(x, probs)
plt.fill_between(x, probs)
plt.fill_between(x1, uniform.pdf(x=x1, loc=1, scale=4), color="r")
plt.xlabel("Time required for bug fixing")
plt.ylabel("Probability")
plt.title("Continuous Uniform Distribution: X ~ U(1,5)")
plt.show()

# %% [markdown]
# In the above graph, the reg region represent P(X>2). Let's calculate the probability that that that a randomly selected software debugging requires more than two hours. We will use uniform.cdf() for this.

# %%
1 - uniform.cdf(x=2, loc=1, scale=4)

# %% [markdown]
# **Let's calculate the 50th percentile of software debugging time.**
# 
# ppf(): It is used to calculate the percentile point given probability. It works opposite of cdf()

# %%
uniform.ppf(q=0.5, loc=1, scale=4)

# %% [markdown]
# ### Conclusion:  
# 
# There is a 50% chance that a randomly selected software debugging requires less than three hours.
# 
# There is a 75% chance that a randomly selected software debugging requires more than two hours.
# 
# The 50th percentile of the software debugging time is 3 hours.

# %% [markdown]
# # <a name='link3'>**Normal Distribution**</a>

# %% [markdown]
# ## Problem statement
# 
# A testing agency wants to analyze the complexity of SAT Exam 2020. They have collected the SAT scores of 1000 students in "sat_score.csv". Let's answer some of the questions that will help to decide the complexity of SAT exam 2020.
# 
# 
#  
# 1. Calculate the probability that a student will score less than 800 in SAT exam
# 2. Calculate the probability that a student will score more than 1300 in SAT exam
# 3. Calculate the minimum marks a student must score in order to secure 90th percentile
# 4. Calculate the minimum marks a student must score in order to be in the top 5%
# 
# 

# %% [markdown]
# ### Reading the Data into the Dataframe

# %%
sat_score = pd.read_csv("sat_score.csv")
sat_score.head()

# %% [markdown]
# ### Calculating the mean and standard deviation (parameters) of the SAT score 
# 
# 

# %%
# import the required function
from scipy.stats import norm

# estimate the mean and standard deviation of the SAT scores data
mu = sat_score["score"].mean()
sigma = sat_score["score"].std()
print("The estimated mean is", round(mu, 2))
print("The estimated standard deviation is", round(sigma, 2))

# %% [markdown]
# ### Plotting the Distribution 
# 
# It  will help us analyze the shape of the data and visualize the PDF of normal distribution using the parameters (mean (mu) and Standard deviation (sigma)) from the data.

# %%
# calculate the pdf of SAT scores using norm.pdf()
density = pd.DataFrame() # create an empty DataFrame
density["x"] = np.linspace(
    sat_score["score"].min(), sat_score["score"].max(), 100
) # create an array of 100 numbers in between the min and max score range and store it in the first column of the empty DataFrame
density["pdf"] = norm.pdf(density["x"], mu, sigma) # calculate the pdf() of the created numbers and store it in another column named 'pdf'

fig, ax = plt.subplots() # create the subplot
sns.histplot(sat_score["score"], ax=ax, kde=True, stat="density") # plot the distribution of data using histogram
ax.plot(density["x"], density["pdf"], color="red") # plot the pdf of the normal distribution
plt.title("Normal Distribution") # set the title
plt.show() # display the plot

# %% [markdown]
# **Insight:**  As you can see in the above plot, there are two curves red and blue. Blue curve represents the shape of data distribution and the red curve represents the PDF (Probability density function). This data is approximately normal. Thus, we can assume this data distribution to be normal and perform our calculations based on the normality assumption.
# 
# X ~ N(mu, sigma)

# %% [markdown]
# **Calculate the probability that a student will score less than 800 in SAT exam.**

# %%
# find the cumulative probability
# norm.cdf() calculates the cumulative probability
prob_less_than_800 = norm.cdf(800, mu, sigma)
print(
    "The probability that a student will score less than 800 is",
    round(prob_less_than_800, 4),
)

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
plt.plot(density["x"], density["pdf"]) # plot the pdf of the normal distribution
plt.axvline(x=800, c="r") # draw a red vertical line at x = 800
x1 = np.linspace(density["x"].min(), 800, 50) # create an array of 50 numbers between min SAT score and 800
plt.fill_between(x1, norm.pdf(x1, mu, sigma), color="r") # fill the specified region with red color
plt.xlabel("Score") # set the x-axis label
plt.ylabel("Probability") # set the y-axis label
plt.title("Normal Distribution") # set the title
plt.show() # display the plot

# %% [markdown]
# **Calculate the probability that a student will score more than 1300 in SAT exam.**

# %%
# find the cumulative probability and subtract it from 1 to calculate the probability that a student will score more than 1300
prob_greater_than_1300 = 1 - norm.cdf(1300, mu, sigma)
print(
    "The probability that a student will score more than 1300 is",
    round(prob_greater_than_1300, 4),
)

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
plt.plot(density["x"], density["pdf"])
plt.axvline(x=1300, c="r")
x1 = np.linspace(1300, density["x"].max(), 50)
plt.fill_between(x1, norm.pdf(x1, mu, sigma), color="r")
plt.xlabel("Score")
plt.ylabel("Probability")
plt.title("Normal Distribution")
plt.show()

# %% [markdown]
# **Calculate the minimum marks a student must score in order to be in the 90th percentile**

# %%
# calculate the 90th percentile score using ppf() function
# norm.ppf() calculates the percentile point
score_90th_percentile = norm.ppf(0.90, mu, sigma)
print("The 90th percentile score should be", round(score_90th_percentile))

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
plt.plot(density["x"], density["pdf"])
plt.axvline(x=score_90th_percentile, c="r")
plt.xlabel("Score")
plt.ylabel("Probability")
plt.title("Normal Distribution")
plt.show()

# %% [markdown]
# **Calculate the minimum marks a student must score in order to be in the top 5%**

# %%
# calculate the 95th percentile score using ppf() function
score_top_five_percent = norm.ppf(0.95, mu, sigma)
print("The minimum score to be in top 5% should be", round(score_top_five_percent))

# %%
# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.
# Of course you do not 'need' to create the following visualization to answer the question above.
# You can directly use the cdf function for probability calculations.
plt.plot(density["x"], density["pdf"])
plt.axvline(x=score_top_five_percent, c="r")
plt.xlabel("Score")
plt.ylabel("Probability")
plt.title("Normal Distribution")
plt.show()

# %% [markdown]
# **Conclusion:** 
# 
# 1) Only 15.51% of students will score below 800 and 7.62% of students will score above 1300. It shows that the 2020 SAT exam's complexity is moderate. 
# 
# 2) Students should score at least 1269 to secure the 90th percentile.
# 
# 3) Students should score at least 1344 to be in the top 5%.

# %% [markdown]
# ### Standardization of Normal Variables
# 
# Suppose we know that the SAT scores are normally distributed with mean 1000 and standard deviation 200 and ACT scores are normally distributed with mean 20 and standard deviation 5. 
# 
# A college provides admission only on the basis of SAT and ACT scores. The college admin decides to give the top performer fellowship to the student who has performed the best among all applicants. The highest score received from applicants who appeared for SAT is 1350 and the highest score received from applicants who appeared for ACT is 30. 
# 
# Help the college to choose the best candidate for the fellowship!

# %%
# plot the two distribution for SAT and ACT scores
from scipy.stats import norm
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,4))
x = np.linspace(400, 1600, 1000)
ax1.plot(x, norm.pdf(x, loc = 1000, scale = 200), color = 'b')
ax1.set_title('Normal Distribution of SAT scores')
ax1.set_xlabel('SAT scores')
ax1.set_ylabel('Probability')
ax1.axvline(1350, ymax = 0.23, linestyle = '--', color = 'green')
x1 = np.linspace(1, 36, 100)
ax2.plot(x1, norm.pdf(x1, loc = 20, scale = 5), color = 'r')
ax2.set_title('Normal Distribution of ACT scores')
ax2.set_xlabel('ACT scores')
ax2.set_ylabel('Probability')
ax2.axvline(30, ymax = 0.18, linestyle = '--', color = 'green')
plt.show()

# %% [markdown]
# In the above plot, the blue curve represents the distribution of SAT scores and the red curve represents the distribution of ACT scores. The highest scores of the applicants in SAT and ACT exams are dotted with green lines in the respective distributions. However, it is difficult for us to compare the raw highest scores in the above plot. Thus, we need to standardize the two scores and compare their Z-scores.

# %%
# find the Z-score of highest scorer in SAT among all the applicants
top_sat = (1350 - 1000) / 200
print('The Z-score of highest scorer in SAT among all the applicants', top_sat)
# find the Z-score of highest scorer in ACT among all the applicants
top_act = (30 - 20) / 5
print('The Z-score of highest scorer in ACT among all the applicants', top_act)

# %% [markdown]
# Let's plot the standard normal distribution and visualize the above standardized scores.

# %%
# plot the standard normal distribution
# and visualize the standardized scores
# We are plotting the distributions here to better visualize the calculations.
fig, ax = plt.subplots()
x = np.linspace(-4,4,50)
ax.plot(x, norm.pdf(x, loc = 0, scale = 1), color = 'b')
ax.set_title('Standard Normal Distribution')
ax.set_xlabel('Z-scores')
ax.set_ylabel('Probability')
ax.axvline(top_sat, ymax = 0.25, linestyle = '--', color = 'green')
ax.axvline(top_act, ymax = 0.16, linestyle = '--', color = 'black')
plt.show()

# %% [markdown]
# In the above plot, the green line represents the standardized highest SAT score of the applicants which is 1.75 standard deviations above the mean and the black line represents the standardized highest ACT score of the applicants which is 2 standard deviations above the mean.
# 
# This means that among the applicants, the highest scorer in ACT performed better than the highest scorer in SAT.
# 
# Thus, the top performer fellowship should be given to the applicant who has scored highest in ACT.


