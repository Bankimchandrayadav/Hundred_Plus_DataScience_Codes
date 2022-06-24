# %% [markdown]
# # About 
# This code demonstrates various matplotlib features described in a public blog: https://www.mygreatlearning.com/blog/matplotlib-tutorial-for-data-visualisation/



# %% [markdown]
# # Libraries
# %% [code]
# import matplotlib
# matplotlib.__version__
import matplotlib.pyplot as plt
import numpy as np 



# %% [markdown]
# # Simple plot
# %% [code] 
# Define data
x = np.linspace(0,50,100)
y = x * np.linspace(100,150,100)
# Plot
plt.plot(x,y)



# %% [markdown]
# # Plot with basic elements added
# %% [code] 
# Define data
x = np.linspace(0,50,100)
y = x * np.linspace(100,150,100)
# Plot
plt.plot(x,y, c='b', linestyle='--', linewidth=2, marker='*', markersize=3, label='SamplePlot')
#  Basic elements
plt.title('Plot with numerous elements added')
plt.xlabel('x label runs here')
plt.ylabel(' y label runs here')
plt.xlim(0, 60)
plt.ylim(0, 15000)
plt.legend()
plt.grid(True)



# %% [markdown]
# # Creating subplots
# %% [code] 
# Firstly lets see the use of `fig, ax` 
x = np.random.rand(50)
y = np.sin(x*2)
fig, ax = plt.subplots()
ax.plot(y)
ax.plot(x)



# %% [markdown]
# # Subplot - 1
# %% [code] 
# Define data
x=np.linspace(0,100,10)
# Plot
fig, axs = plt.subplots(2)
axs[0].plot(x, np.sin(x**2))
axs[1].plot(x, np.cos(x**2))
fig.suptitle('Vertically stacked subplots')



# %% [markdown]
# # Subplot - 2
# %% [code] 
# Define data 
x=np.linspace(0,100,10)
# Plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x, x**2)
ax2.plot(x, x**3)
ax3.plot(x, np.sin(x**2))
ax4.plot(x, np.cos(x**2))
fig.suptitle('Horizontal plots')



# %% [markdown]
# # Subplot - 3 
# %% [code] 
# Define data 
# Plot 
fig, axs = plt.subplots(2, 2)
# add the data referring to row and column
axs[0,0].plot(x, x**2,'g')
axs[0,1].plot(x, x**3,'r')
axs[1,0].plot(x, np.sin(x**2),'b')
axs[1,1].plot(x, np.cos(x**2),'k')
# add title
fig.suptitle('matrix sub plots')



# %% [markdown]
# # Notes
# 1. The above is same as Subplot -2 but the way of defining axes is diffferent.



# %% [markdown]
# # Figure object
# 1. The object figure is a container for showing the plots and is instantiated by 
# calling `figure()`.
# %% [code] 
# Define data
X = np.array([1,2,3,4,5,6,8,9,10])
Y = X**2
# Plot
fig = plt.figure(figsize=(10,3),facecolor='y',edgecolor='r',linewidth=5)
plt.plot(X,Y);



# %% [markdown]
# # Axes object 
# 1. Axes is the region of the chart with data, we can add the axes to the figure using the `add_axes()` method.  
# 2. This method requires the following four parameters i.e., `left`, `bottom`, `width`, and `height` where these parameters are: 
    # - `Left` - position of axes from left of figure
    # - `bottom` - position of axes from the bottom of figure
    # - `width` - width of the chart
    # - `height` - height of the chart
# %% [code] 
# Define data 
y = [1, 5, 10, 15, 20,30]
x1 = [1, 10, 20, 30, 45, 55]
x2 = [1, 32, 45, 80, 90, 122]
# create the figure
fig = plt.figure()
# add the axes
ax = fig.add_axes([0,0,2,1])  # note this 
l1 = ax.plot(x1,y,'ys-') 
l2 = ax.plot(x2,y,'go--')
# add additional parameters
ax.legend(labels = ('line 1', 'line 2'), loc = 'lower right') 
ax.set_title("usage of add axes function")
ax.set_xlabel('x-axix')
ax.set_ylabel('y-axis')
plt.show()  



# %% [markdown]
# # Bar chart
# %% [code] 
# Define data 
subject = ['maths','english','science','social','computer']
marks =[70,80,50,30,78]
# Plot vertical (note arg `bottom` and `yerr`)
plt.bar(subject,marks,width = 0.5,bottom=10,align ='center',edgecolor='r',linewidth=2,tick_label=subject, yerr=np.std(marks))
# Plot horizontal (note arg `xerr`)
plt.barh(subject,marks,xerr=np.std(marks))



# %% [markdown]
# # Pie chart
# %% [code] 
# Data
Tickets_Closed = [10, 20, 8, 35, 30, 25]
Agents = ['Raj', 'Ramesh', 'Krishna', 'Arun', 'Virag', 'Mahesh']
# Plot - regular
plt.pie(Tickets_Closed, labels = Agents)
# Plot - exploded
# autopct - used to show the % of contributions for the widgets
explode = [0.2,0.1,0,0.1,0,0]
plt.pie(Tickets_Closed, labels = Agents, explode=explode, autopct='%1.1f%%' )



# %% [markdown]
# # Scatter plot 
# %% [code] 
# Plot with regular marker size
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x,y)
# Plot with scaled marker size and diff colors
size = 150*np.random.randn(100)
colors = 150*np.random.randn(100)
plt.scatter(x, y, s=size, c = colors, marker ='o', alpha=0.7)



# %% [markdown]
# # Notes 
# Note the arguments of `scatter()`:
# - `norm` – to normalize the data (scaling between 0 to 1)
# - `alpha` – transparency of point
# - `marker` – type of marker 
# - `color` – to set the color of the points
# - `size` – to manage the size of the points



# %% [markdown]
# Histogram - Single
# %% [code] 
data = np.random.randn(1000)
plt.hist(data, facecolor ='y',linewidth=2,edgecolor='k', bins=30, alpha=0.6)



# %% [markdown]
# # Histogram - Multiple extended on same plot
# %% [code]
data1 = np.random.normal(25,10,1000)
data2 = np.random.normal(200,5,1000)
a = plt.hist(data1,facecolor = 'yellow',alpha = 0.5, edgecolor ='b',bins=50);
b = plt.hist(data2,facecolor = 'orange',alpha = 0.8, edgecolor ='b',bins=30);
plt.show()



# %% [markdown]
# # Save figure 
# %% [code] 
# Define data
x = np.arange(6)
labels = [5,10,20,25,30,40]
# Plot
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, label=labels)
plt.title('Saving as Image')
ax.legend()
fig.savefig('../02_OutFiles/saveimage.png')



# %% [markdown]
# # Reading image
# %% [code] 
import matplotlib.image as mpimg
image = mpimg.imread("../02_OutFiles/saveimage.png")
plt.imshow(image)
plt.show()



# %%