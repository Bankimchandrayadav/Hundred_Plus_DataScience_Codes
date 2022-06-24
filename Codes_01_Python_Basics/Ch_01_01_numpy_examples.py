# %% [markdown]
# # About 
# This code is a demonstration of numpy package.



# %% [markdown]
# # Libraries
# %% [code]
import numpy as np



# %% [markdown]
# # Numpy functions
# %% [code] 
print(np.cos(np.pi))
print(np.sqrt(1.21))
print(np.log(np.exp(5.2)))



# %% [markdown]
# # Creating a vector and a matrix
# %% [code]
# Vector - just pass a list 
vec = np.array([1,2,3])
print(vec)
# Matrix - pass a list of lists
mat = np.array([[1,2,1],[4,5,9],[1,8,9]])
print(mat)
# Matrix transpose
print(mat.T)



# %% [markdown]
# # Creating a vector with np.arange()
# %% [code]
# syntax = np.arange(start(inclusive), end, step size)
vec2 = np.arange(0,15)
print(vec2)
vec3 = np.arange(3,21,6)  
print(vec3)



# %% [markdown]
# # Creating a vector with np.linspace()
# %% [code]
vec4 = np.linspace(0,5,10)
print(vec4)
# Reshape any vector
vec4.reshape(5,2)
vec4_reshaped = vec4.reshape(5,2)
print('\n\nReshaped and original vectors:\n')
print(vec4_reshaped)
print(vec4)  # original remains unchanged



# %% [markdown]
# # Creating vectors/matrices - more ways
# %% [code]
# A zeros matrix - pass a list or a tuple
mat2 = np.zeros([5,3])  
print(mat2, '\n')
# A ones matrix - pass a list or a tuple
mat3 = np.ones((3,5))  
print(mat3, '\n')
# Identity matrix - pass a number
mat4 = np.eye(5)
print(mat4)



# %% [markdown]
# # Element wise operations
# %% [code]
# Create arrays
vec5 = np.arange(1,6)
vec6 = np.arange(3,8)
print(vec5, '\n')
print(vec6, '\n')
# Element wise operations
print('Addition:', vec5+vec6)
print('Multiplication:',vec5*vec6)
print('Division by a scalar:',1/vec5)
print('Square root:',np.sqrt(vec6))



# %% [markdown] 
# # Matrix multiplication
# %% [code]
print('First Matrix:\n', mat, '\n')
print('Second Matrix/Vector:\n', vec, '\n')
# Product - inner dimensions have to be same
product = np.matmul(mat,vec)
print('Matrix product:\n', product)



# %% [markdown] 
# # Matrix solutions
# %% [code]
# mat*vec=product: find vec
print(np.linalg.solve(mat,product))
# Find inverse
print(np.linalg.inv(mat))



# %% [markdown]
# # Find unique values in an array
# %% [code]
vec7 = np.array(['blue','red','orange','purple','purple','orange','Red',6])
print(vec7)
print(np.unique(vec7))



# %% [markdown]
# # Notes 
# 1. An imp thing to note here is that `np.array` accepts values of same datatype, and it typecasts the integer 6 to string dynamically, to make all of same datatype.



# %% [markdown]
# # Generate samples of a random variable
# %% [code]
# Uniform random variable
rand_mat = np.random.rand(5,5) 
print(rand_mat, '\n')
# Standard normal random variable
rand_mat2 = np.random.randn(10,5) 
print(rand_mat2)



# %% [markdown]
# # Notes
# 1. In `rand_mat`, all entries are in the range 0 to 1 while it's not in `rand_mat2`. 
# 2. Also, the mean of a uniform random variable is half (0.5) while the mean and std dev of a standard normal variable is 0 and 1 respectively.



# %% [markdown] 
# # numpy for statistics
# %% [code]
print(np.mean(rand_mat))
print(np.std(rand_mat2))



# %% [markdown] 
# # min and max of an array
# %% [code]
print(np.min(rand_mat))
print(np.max(rand_mat2))



# %% [markdown] 
# # Accessing vector values - single value
# %% [code]
rand_vec = np.random.randn(19)
print(rand_vec)
print(rand_vec[6])



# %% [markdown] 
# # Accessing vector values - multiple values
# %% [code]
print(rand_vec[4:9])



# %% [markdown] 
# # Accessing vector values - non-consecutive values
# %% [code]
# Firstly create the non-consecutive index array
print(np.arange(0,15,3))
# Then access array values at those indices
print(rand_vec[np.arange(0,15,3)])



# %% [markdown] 
# # Accessing matrix values - single value
# %% [code]
print(rand_mat)
print(rand_mat[1][2])  # will work in lists
print(rand_mat[1,2])  # won't work in lists



# %% [markdown] 
# # Accessing matrix values - multiple values
# %% [code]
print(rand_mat[0:2,1:3])



# %% [markdown] 
# # Modifying values in a vector
# %% [code]
print(rand_vec, '\n')
rand_vec[3:5] = 4
print(rand_vec, '\n')
rand_vec[3:5] = [1,2]
print(rand_vec, '\n')



# %% [markdown] 
# # Modifying values in a matrix
# %% [code]
print(rand_mat, '\n')
rand_mat[1:3,3:5] = 0
print(rand_mat)



# %% [markdown] 
# # Modifying values in the copy of an array
# %% [code]
# Copy1=subset of original array
sub_mat = rand_mat[0:2,0:3]
# Copy2=original array
sub_mat1 = rand_mat
# Modify Copy1 and Copy2
sub_mat[:] = 3
sub_mat1[:] = 5
print(sub_mat, '\n')
print(sub_mat1, '\n')
# See if original array also changed?
print(rand_mat)


# %% [markdown] 
# # Notes 
# 1. When we reach to `print(sub_mat)` command, all of its values are shown as 5, and not 3. This is because executing `sub_mat1[:] = 5` changes all the values of `rand_mat` to 5 and `print(sub_mat)` is just accessing the subset [0:2,0:3] of `rand_mat`. 
# 2. Hence, remember that every such operation modifying a copy of numpy array acutally modifies the original array.



# %% [markdown] 
# # Modifying values using the `.copy()` function
# %% [code]
sub_mat2 = rand_mat[0:2,0:3].copy()
sub_mat2[:] = 99
print(sub_mat2)
print(rand_mat)



# %% [markdown] 
# # Acess entries with logicals in arrays
# %% [code]
rand_vec = np.random.randn(15)
print(rand_vec)
print(rand_vec>0)
print(rand_vec[rand_vec>0])



# %% [markdown] 
# # Notes 
# 1. Here, the boolean array needs not be only a conditional output of `rand_vec`, but can be any boolean array of the same size as `rand_vec`.



# %% [markdown] 
# # Acess entries with logicals in matrices
# %% [code]
print(rand_mat2, '\n')
print(rand_mat2>0, '\n')
print(rand_mat2[rand_mat2>0], '\n')



# %% [markdown] 
# # Notes 
# 1. We cannot collapse some values of a matrix and get something that looks like a matrix. We can delete either an entire row or a column and get the output as a matrix, but deleting any particular value and condensing the rest of the entries won't produce a matrix.
# 2. Hence, python transforms `rand_mat2[rand_mat2>0]` into an array. The values are iterated and filtered rowwise.


# %% [markdown] 
# # Modifying values with logicals
# %% [code]
print(rand_vec, '\n')
rand_vec[rand_vec>0.5] = -5
print(rand_vec, '\n')



# %% [markdown] 
# # Saving numpy arrays on disk for later use
# %% [code]
# Single array
np.save('../02_OutFiles/saved_file_name', rand_mat2)
# Multiple arrays at once
np.savez('../02_OutFiles/zipped_file_name', rand_mat=rand_mat,rand_mat2=rand_mat2)



# %% [markdown] 
# # Notes
# 1. In `np.savez()`, we have to provide the names of all arrays in the zipped file



# %% [markdown] 
# # Loading a saved array
# %% [code]
loaded_vec = np.load('../02_OutFiles/saved_file_name.npy')
loaded_zip = np.load('../02_OutFiles/zipped_file_name.npz')
print(loaded_vec, '\n')
print(loaded_zip)
# Individual files names should be called in a zipped array
print(loaded_zip['rand_mat'], '\n')
print(loaded_zip['rand_mat2'], '\n')



# %% [markdown] 
# # Save/load as text files
# We can also save/load as text files...but only single variables
# %% [code]
# Save
np.savetxt('../02_OutFiles/text_file_name.txt',rand_mat,delimiter=',')
# Load - delimiter need to be specified again or else error
# rand_mat_txt = np.loadtxt('../02_OutFiles/text_file_name.txt')  
rand_mat_txt = np.loadtxt('../02_OutFiles/text_file_name.txt',delimiter=',')
print(rand_mat, '\n')
print(rand_mat_txt)



# %%