# %% [markdown]
# # About 
# This code is a practice exercise related to numpy package.



# %% [markdown]
# # Libraries 
# %% [code]
import numpy as np



# %% [markdown]
# # Background
# 1. We have seen the basic data structures of python in the previous codes of Module 1. They are great but lack specialized features for data analysis. Like, adding rows, columns, operating on 2d matrices aren't readily available. So, we will use numpy for such functions.
# 2. Numpy operates on n-dimensional arrays. These are similar to lists and have easier to store 2-d data, but contain homogenous elements. 
# %% [code]
# Initializing numpy array from a list
l1 = [1,2,3,4]
nd1 = np.array(l1)
nd1
# Initializing numpy array from a list from multiple lists
l2 = [5,6,7,8]
nd2 = np.array([l1,l2])
nd2
# Basic properties of array
print('Shape of nd array is:' , nd2.shape)
print('Size of nd array is:' , nd2.size)
print('Data type of nd array is:' , nd2.dtype)



# %% [markdown]
# # Question 1
# Create an identity 2d-array or matrix (with ones across the diagonal).
# %% [code]
np.identity(5)



# %% [markdown]
# # Question 2
# Create a 2d-array or matrix of order 3x3 with values = 9,8,7,6,5,4,3,2,1 arranged in the same order.
# %% [code]
# Using `np.matrix()` (a matrix is limited to 2 dimensions)
d1 = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
print(d1)
print(type(d1),'\n')
# Using np.array() (more general)
d2 = np.array(([9,8,7],[6,5,4],[3,2,1]))
print(d2)
print(type(d2),'\n')
# We can also use the arange function and then reshape the array into the desired matrix
d3 = np.arange(start = 9, stop = 0, step = -1)
d3 = d3.reshape(3,3)
print(d3)
print(type(d3))



# %% [markdown]
# # Question 3
# Interchange both the rows and columns of d3 matrix, i.e., transpose.
# %% [code]
print(d3.T)


# %% [markdown]
# # Question 4
# Add (+1) to all the elements in d3 matrix.
# %% [code]
d3 + 1
 


# %% [markdown]
# # Notes
# 1. Similar to addition of a scalar in the above cell, we can do other operations like scalar substraction, division and multiplication.



# %% [markdown]
# # Question 5
# Find the mean of all elements in the given matrix `nd6`: </br>
# `[[  1   4   9 121 144 169]` </br>
#  `[ 16  25  36 196 225 256]` </br>
#  `[ 49  64  81 289 324 361]]` </br>
# %% [code]
# Firstly, define the matrix
nd6 = np.array([[1, 4, 9, 121, 144, 169], [16, 25, 36, 96, 25, 56],[49, 64, 81, 289, 324, 361]])
# Then find mean
nd6.mean()



# %% [markdown]
# # Question 7
# Find the dot product of the two matrices - `d3` and `nd6`
# %% [code]
d3
nd6
np.dot(d3, nd6)



# %% [markdown]
# # Notes
# Dot product of the above matrices is possible because the the shapes of `d3` and `nd6` are `3x3 (mxn)` and `3x3 (nxp)`. It produces the matrix of shape `3x3 (mxp)`.



# %%