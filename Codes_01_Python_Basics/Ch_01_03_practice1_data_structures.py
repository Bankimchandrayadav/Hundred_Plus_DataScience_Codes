# %% [markdown]
# # About 
# This code is a practice exercise related to python data structures.



# %% [markdown] 
# # Libraries
# %% [code]
import numpy as np



# %% [markdown]
# # Background
# Sequences in Python are data structures that hold objects in an ordered array. 
# Now, we will work on **Lists**, the most common sequence data types in Python.
# %% [code]
# Example 
l1 = ['learning', "Python", 'is fun?', True]
print(l1)
# Lists can also be created by using list() function. 
# Example
l2 = list(("learning", "for", "life", True))
print(l2)



# %% [markdown]
# # Question 1 
# Add 10 to list `l1` given above.
# %% [code]
l1.append(10)
l1



# %% [markdown]
# # Question 2
# Remove 10 from the list `l1`.
# % [code]
l1.remove(10)
l1



# %% [markdown]
# # Notes 
# 1. If we type `l1.remove(1)` it doesn't throw and error (as expected) even though 1 is not in the list!



# %% [markdown]
# # Question 3
# Join the two lists `l1` and `l2`
# %% [code]
l1 = ['learning', "Python", 'is fun?', True]
l2 = list(("learning", "for", "life", True))
# Using + operator
l1+l2
# Using `extend()` function
l1.extend(l2)
print(l1)



# %% [markdown]
# # Question 4
# Find range and mean of `l3`.
# %% [code]
l3 = [2,4,6,8]
# Without any library
# Range of l3
print('Range:', max(l3)-min(l3))
# Mean of l3
print('Mean:', sum(l3)/len(l3))
# With library
import numpy as np 
print('Range:', np.ptp(l3))
print('Mean:', np.mean(l3))



# %% [markdown]
# # Question 5
# Append the given sequence of numbers `0,1,3,3,5,5,7,9` to `l3` and then count the 
# no. of occurences of `5` in `l3`.
# %% [code]
# Way 1
(l3 + [0,1,3,3,5,5,7,9]).count(5)
# Way 2
l3.extend([0,1,3,3,5,5,7,9])  
l3
# Way 3 - doesn't work
# l3.append([0,1,3,3,5,5,7,9])  # whole list is added as a single entity
# l3
# l3.append(0,1,3,3,5,5,7,9)  # throws error
# l3


# %% [markdown]
# # Question 6
# Sort and print `l3` in ascending and descending order.
# %% [code]
l3
l3.sort()
l3
l3.sort(reverse = True)
l3



# %% [markdown]
# # Question 7
# Define a function with name `sum_3` which can take 3 numbers as input, and returns 
# their sum.
# %% [code]
def sum_3(a,b,c):
    return a+b+c
sum_3(2,3,5)



# %% [markdown]
# # Question 8
# Write the same function `sum_3` using a lambda function. </br>
# Lambda functions  are anonymous functions or no name functions, which can be considered when we use a function only once, e.g., `f = lambda x, y: x + y`, then `f
# (1) = 2`.
# %% [code]
f = lambda x,y,z: x+y+z
f(1,2,3)



# %%