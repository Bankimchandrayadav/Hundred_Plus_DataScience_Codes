# %% About 
# 1. This code introduces diferent variable types in python.



# %% [markdown]
# # With a single hashtag we get a big section header
# ## With double hashtags we get a subsection
# ## LaTeX
# We can also use LaTeX commands in-line with single dollar signs:  $\int_0^\infty f(x) dx$. We can add LaTeX equations centered on their own lines with double dollar signs: $$\sum_{i=1}^\infty \frac{1}{2^i}$$ 



# %% Comments and assignment
# We can add comments to code cells using a hashtag with 'ctrl + /' or  'cmd + /'
# Assign a variable to a literal value
a=3 
print('five times a is',5*a,'and 3 multiplied by a is',3*a)
a=2
print('five times a is',5*a,'and 3 multiplied by a is',3*a)



# %% Inspect data type
print('a is of type',type(a))
b = 2.1
print('b is of type',type(b))
c = float(a)*b
print('c is of type',type(c), 'and its value is',c)
d = a*b
print('d is of type',type(c), 'and its value is',d)



# %% Notes
# 1. In C or C++, int * float would have resulted in lowest data type i.e., int 
# 2. In python, result will be float. As seen above, we can explicitly typecast `a` into float before multiplication or not, the result type would be same.



# %% [markdown]
# # Collections of variables


# %% Lists - creating and indexing
simple_list = ['Dan',2,3,8,'python',2.71]
print(simple_list)
# Indexing
print(simple_list[0])  # first val
print(simple_list[3])  # fourth val
print(simple_list[-1])  # last val
print(simple_list[-2])  # second last val
# Get length of list
print(len(simple_list))



# %% Lists - modifying
# Replace a value at an index
simple_list[3] = 52
print(simple_list) 
# Add a value to the last
simple_list.append('to the back')
print(simple_list)
print(len(simple_list))  # len increased by 1
# Remove a value from an index
simple_list.pop(4)
print(simple_list)



# %% Lists - nice way to initialize with same entries
repeated_list = [5]*6
print(repeated_list)



# %% Lists - use lists as entries of a list
simple_list[1] = [1,2,3]
print(simple_list)
print(simple_list[1])
print(simple_list[1][1])



# %% Lists - copying can be tricky
# Copy by assigning 
list2 = simple_list
print(list2)
print(simple_list)
# Modifiy new list
list2[1] = 0
# See how both lists change
print(list2)
print(simple_list)



# %% Lists - use the copy method to prevent the above behavior
# Copy using `.copy()` function
list3 = simple_list.copy()
print(list3)
print(simple_list)
# Modify new list 
list3[0] = 'Mitchell'
# See how original list remains preserved
print(list3)
print(simple_list)



# %% Tuples - creation
simple_tuple = (12,42,11,99,2351)
print(simple_tuple)
print(simple_tuple[1])



# %% Tuples - not possible to change entries 
# Trying it will throw an error
# simple_tuple[0] = 5



# %% Tuples - workaround to change entries 
# Typecast to a list and modify
dummy = list(simple_tuple)
dummy[0] = 5
# Typecast back to tuple
simple_tuple = tuple(dummy)
print(simple_tuple)



# %% Sets - creation
simple_set = {11,-2,'water',-2}
# `-2` will only show up once
print(simple_set)



# %% Sets - indexing not possible
# Will throw an error
# print(simple_set[1])



# %% Sets - alternvative to indexing
print('water' in simple_set)  # applies to other collections too



# %% Sets - can't modify but add and remove
# you can't change values but you can add and remove entries from a set
simple_set.add(72)
print(simple_set)
simple_set.remove('water')
print(simple_set)



# %% Dictionaries - creating
simple_dict = {
    "brand": "Apple.",
    "product": "iPhone",
    "model": "11"
}
print(simple_dict)



# %% Dictionaries - indexing through its keys
print('I bought an',simple_dict['product'],"model",simple_dict['model'],'from',simple_dict['brand'])



# %% Dictionaries - modifying
simple_dict["brand"] = "Apple Inc."
print('I bought an',simple_dict['product'],"model",simple_dict['model'],'from',simple_dict['brand'])



# %% Dictionaries - adding values
simple_dict['color'] = 'sea green'
print('I bought a',simple_dict["color"],simple_dict['product'],"model",simple_dict['model'],'from',simple_dict['brand'])    



# %% Accessing data in lists
# Define list
simple_list = [1,5,2,7,3,66,1923,11]
# Access multiple values 
print(simple_list[2:5])
print(simple_list[2:3])
# Access values using -ve indices
print(simple_list[-5:-1])



# %% Notes 
# 1. Remember in indexing or rather slicing the number to the left of the colon is inclusive, and the number to the right of the colon is exclusive.



# %%