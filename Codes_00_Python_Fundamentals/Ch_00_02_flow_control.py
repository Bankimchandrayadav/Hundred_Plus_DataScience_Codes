# %% About 
# This code is a demo of the flow control in python



# %% For loops
# 1. It can loop through a list or other types of aggregated variables.
# 2. The body of a loop are determined by tabs. This is also true for conditionals and user defined functions.
counter = 0
simple_list = [0,1,2,3,4,5,6,2143,123,7834]
for i in simple_list:
    # Only the tabbed lines are inside loop
    print(i)
    counter = counter + 1
print('this line is not inside the loop')
print('the loop cycled',counter,'times')



# %% Nested for loop
for i in simple_list[1:4]:
    for j in simple_list[4:7]:
        print(i*j)
    print('outside of j loop')
print('outside of both loops')
    


# %% `range()` function
print(range(6))



# %% Use `range()` in loops
# Default increment by 1
for i in range(4,10):
    print(i)
print('\n')
# Increment by a specific value
for i in range(2,10,3):
    print(i)



# %% Typecast range to list
list(range(6,15,3))



# %% While loops
# 1. while loops are similar to most other languages
i = 4
while i < 10:
    print(i)
    i = i+1
print('outside of loop')



# %% Notes 
# 1. If we remove the line `i=i+1` the condition in the loop will always be true and it'd result in an infinite loop.



# %% Conditionals
# 1. Three type of statements:
    # - if statement
    # - else statement
    # - elif statement



# %% if-else
i = 30
if i<10:
    print(i,'is less than 10')
    print('run this also')
else:
    print(i,'is greater than or equal to 10')
    



# %% if-elif-else
i = 3
if i > 10:
    print(i,'is greater than 10')
elif i <= 3:
    print(i,'is less than 3')
elif i > 4:
    print(i)
else:
    print(i,'is between 3 and 10')
    


# %% Notes:
# 1. Flow breaks at the point where python gets a true condition. Even though other conditions are true after `elif i<=3`, it executes the conditional command and exits. 



# %%