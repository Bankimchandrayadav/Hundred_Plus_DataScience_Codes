# %% About
# This code demonstrates functions in python.



# %% Background:
# There are 2 kinds of functions:
    # 1. defined functions
    # 2. lambda functions (inline)



# %% Defined function - simple
# Define a function that takes an input, squares it, adds 7, then returns the answer
def x2p7(x):
    """    this is my documentation string
    it needs to be in triple double quotes
    this function returns x^2 + 7"""
    y = x*x
    z = y+7
    return z
# Call the function
print('x^2 + 7 = ',x2p7(5))
# Also get the docstring of that function
print(x2p7.__doc__)  



# %% Notes 
# 1. help(x2p7) will also yield the docstring of that function.



# %% Defined function - complicated
# Define the function
def complicated_function(x,y):
    lenx = len(x)
    leny = len(y)
    z = [0]*(lenx*leny)
    counter = 0
    for i in x:
        for j in y:
            z[counter] = i*j
            counter = counter+1
    return z
# Call the function
output = complicated_function([1,2,3,4],[34,234,31,888])
print(output)



# %% Scope fo variables
# Var defined within function are not accessible outside
# print(lenx)  # will cause error
# Var defined outside function are accessible within function
outside_var = 213
def a_function(x):
    return outside_var*x
print(a_function(2))
print(outside_var)



# %% Global variables within functions
# Define function
def another_function(x):
    global global_var
    global_var = 5
    return global_var*x
# Call function
print(another_function(4))
print(global_var)



# %% Notes 
# 1. It is essential that the declaration of the variable as global and the value assignemnt to that variable are done on seperate lines as shown above, or it will cause error. 



# %% Lamda functions (Inline functions)
# Example 1 - rewriting first function as a lamda function
x2p7v2 = lambda x: x*x+7
print(x2p7v2(5))
# Example 2 - multiple inputs
another_lambda = lambda x,y,z: x*y + y*z + x/y
print(another_lambda(2,5,6))



# %%