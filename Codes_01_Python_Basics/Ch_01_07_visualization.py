# %% [markdown]
# # About 
# 1. This code is a demo of basic visualizations in python. 



# %% [markdown]
# # Libraries
# %% [code]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)  



# %% [markdown]
# # Read data
# %% [code]
auto = pd.read_csv('../01_InFiles/Automobile.csv')
auto.head()



# %% [markdown]
# # Plotting univariate distributions
# 1. The most convenient way to take a quick look at a univariate distribution in 
# seaborn is the `histplot()` or `displot()` function. By default, this will draw a 
# histogram and fit a kernel density estimate (KDE).  
# %% [code]
sns.displot(auto['highway_mpg'], kde=True, label='firstDist', rug=True);
sns.histplot(auto['highway_mpg'], kde=True, label='firstDist'); 
sns.histplot(auto['city_mpg'], kde=False, label='firstDist')
sns.displot(auto['highway_mpg'], kde=True, label='firstDist');
# Use `rugplot` to put a tic mark for every data point
sns.rugplot(auto['city_mpg'])



# %% [markdown]
# # Notes 
# 1. Calculus is how we get the continuous plot (kde) from the histogram. 
# 2. `rug` adds valuable information, such as it shows there is only one point in the second last bin of the above histogram. `rug` plots are informative.



# %% [markdown]
# # Plotting bivariate distributions
# 1. Useful to visualize a relationship between two variables. 
# 2. The easiest way to do this in seaborn is to use the `jointplot()` function, 
# which creates a scatterplot of the two variables along with the histograms of each 
# next to the corresponding axes.
# %% [code]
sns.jointplot(x=auto['engine_size'], y=auto['horsepower'])  # w/o semicolon
sns.jointplot(x=auto['engine_size'], y=auto['horsepower']);  # with semicolon



# %% [markdown]
# # Notes 
# 1. Putting a semicolon at the end of a plot command hides the object name in output. 



# %% [markdown]
# # Joint plot with regression line 
# %% [code]
sns.jointplot(x=auto['engine_size'], y=auto['horsepower'], kind="reg")



# %% [markdown]
# # Hex Bin Plots
# A hex bin plot splits the 2D area into hexagons and the number of where the points 
# in each hexagon determines the shade of the color of that hexagon.
# %% [code]
sns.jointplot(x=auto['engine_size'], y=auto['horsepower'], kind="hex");



# %% [markdown]
# # Kernel Density Estimation
# %% [code]
sns.jointplot(x=auto['engine_size'], y=auto['horsepower'], kind="kde");



# %% [markdown]
# # Visualizing pairwise relationships in a dataset
# %% [code]
sns.pairplot(auto[['normalized_losses', 'engine_size', 'horsepower']]);



# %% [markdown]
# # Strip plot
# 1. It is just a scatterplot but with categorical variable on one axis and continuous on the other. 
# 2. A problem here is that the points usually overlap which makes it difficult to see the full distribution of data. One easy solution is to adjust the positions along the categorical axis by toggling `jitter=True`.
# %% [code]
sns.stripplot(x=auto['fuel_type'], y=auto['horsepower'], jitter=False)
sns.stripplot(x=auto['fuel_type'], y=auto['horsepower'], jitter=True)



# %% [markdown]
# # Swarmplot - a variation of strip plot
# It avoids overlapping along the categorical axis too by binning the points. 
# %% [code]
sns.swarmplot(auto['fuel_type'], auto['horsepower']);



# %% [markdown]
# # Boxplots 
# %% [code]
sns.boxplot(x=auto['number_of_doors'], y=auto['horsepower']);



# %% [markdown]
# # Notes 
# 1. Bottom to top, its Q1, Median and Q3 in the box. The lower whisker extends to a distance of 1.5 IQR from Q1, OR to the smallest value, (whichever distance is smaller). Similarly, the upper whisker extends upto the 1.5 IQR (Q3-Q1) from Q3, OR upto the largest value (whichever distance is smaller). The distance 1.5 IQR arises from a general rule of thumb of statistics to detect outliers. 
# 2. Overall, the box contains 50% of the data with 25% of the data below the box and 25% of the data above the box. 
# 3. Skewness - A boxplot can also tell about the shape of the distribution. If the data doesn't go pretty far lower as compared to how far it goes higher, then its a right skewed distribution. Both the above plots are right skewed.  
# 4. Other observations:
    # - Here the first plot shows that 50% of the two door cars have horsepower less than ~100 and the other 50% has horsepower greater than ~100. 
    # - Next, 75% of the two door cars have hp < ~130 and 25% have hp > ~130, and, 25% of the two door cars have hp < 75 while 75% of two door cars have hp > 75. 



# %% [markdown]
# # Boxplot - with hue 
# %% [code]
sns.boxplot(x=auto['number_of_doors'], y=auto['horsepower'], hue=auto['fuel_type']);



# %% [markdown]
# # Notes
# 1. A subcategory is added with hue.
# 2. There is no  middle line in the boxplots of diesel cars probably because there aren't many data points, and the median is close to either Q1 or Q3. 
# 3. The diesel cars don't show any outliers like the petrol cars. The reason would be that the distance of the largest and smallest point from Q3 and Q1 would be less than than Q3+1.5*IQR and Q1-1.5*IQR, respectively.



# %% [markdown]
# # Bar plots
# %% [code]
sns.barplot(x=auto['body_style'], y=auto['horsepower'])
sns.barplot(x=auto['body_style'], y=auto['horsepower'], hue=auto['fuel_type'])



# %% [markdown]
# # Notes
# 1. The above graph plots the mean of the dataset, separated in categories. When there are multiple observations in each category, it uses bootstrapping to compute a confidence interval around the estimate and plots that using error bars. 
# 2. The vertical black line is the error bar (95% confidence interval).
# 2. Bar plots start at 0, which can sometimes be misleading and sometimes be practical if zero is a number we want to compare to.



# %% [markdown]
# # Countplot
# 1. A special case of the bar plot is when we want to show the number of observations in each category rather than computing the mean.
# 2. This is similar to a histogram but drawn over a categorical, rather than 
# quantitative variable. 
# %% [code]
sns.countplot(x=auto['body_style'], hue=auto['fuel_type']);



# %% [markdown]
# # Point plots
# 1. Rather than showing a full bar, this function just plots the point estimate and confidence interval. Additionally, pointplot connects points from the same hue category. 
# 2. This makes it easy to see how the main relationship is changing as a function of 
# a second variable, because our eyes are quite good at picking up on differences of 
# slopes.
# %% [code]
# With lines
sns.pointplot(x=auto['body_style'], y=auto['horsepower'], hue=auto['number_of_doors'])
# Without lines
sns.pointplot(x=auto['body_style'], y=auto['horsepower'], hue=auto['number_of_doors'], linestyles="")



# %% [markdown]
# # Catplots  - Various kinds
# %% [code]
# Box plot
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="box")
# Violin plot - it draws the kernel density estimate and then flips it around the vertical axis
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="violin")
# Point plot
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="point")
# Bar plot
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="bar")
# Strip plot
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="strip")
# Swarm plot
sns.catplot(x="fuel_type", y = "horsepower", hue="number_of_doors", col="drive_wheels", data=auto, kind="swarm")
# Count plot - can't have both x and y
sns.catplot(x="fuel_type", hue="number_of_doors", col="drive_wheels", data=auto, kind="count")




# %% [markdown]
# # Function to draw linear regression models
# `lmplot()` plots the linear relationship b/w two var - the best fit line and confd. 
# intv.
# %% [code]
sns.lmplot(y="horsepower", x="engine_size", data=auto);
sns.lmplot(y="horsepower", x="engine_size", hue="fuel_type", data=auto);



# %%