"""
This file will show computations involving simple functions
"""

# Simple Hello World function
print("This is the simple Hello World Function")


def func():
    print("Hello")
    print('World')


func()

"Passing Data to a function"


def function(a=128, b=2, *args, **kwargs):
    print("a: %d" % a)
    print("b = %d" % b)
    print("args:", args)
    for key, value in kwargs.items():
        print("%s is %s" % (key, value))
    print()


# Calling the default function
function()
# Assign 0 to a and 4 to b
function(0, 4)
# use keywords to assign values to a and b
function(b=16, a=21)
"""
# *args has been used to denote arbitrary positional arguments
# We can assign values to the arbitrary positional arguments as below
"""
function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
"""
# **kwargs is used to pass key-value arguments
# The syntax is "**" before the parameter name
# The argument will be a dictionary
"""
function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, cat='mieu', cow='moo', dog='bark! bark!')


# Use function to return data as an output
def func_data(a, b):
    return a * b


result = func_data(10, 12)
print(result)


# Use function to return multiple data values as an output
def multiple_data():
    return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


result = multiple_data()
print("The list of values is: ", result)

"""
perform a few computations and return results

"""


def fibs(num):
    fibs_result = [0, 2]
    for i in range(2, num):
        a = fibs_result[i - 1] + fibs_result[i - 2]
        fibs_result.append(a)
    return fibs_result


print("\n Fibs results: \n", fibs(10))

"""
Lambda could be used to define anonymous functions

I took too long to understand the concept of lambda when I was first taught in the University of Stavanger

Now I am so excited that I now understand these concepts

def (parameters):
    return expression
"""

a = lambda x, y: x * y  # x and y are parameters while x*y is an expression
print("\n The first lambda expression \n", a(12, 10))

"""
Higher order functions

this is a function that takes a function as an argument, or return a function

zip function can join two sequences together
"""
a = [1, 2, 3]
b = ['a', 'b', 'c']
print("\nThe zipped values are:")
for values in zip(a, b):
    print(values)

"""
Other higher order functions are map, filter and sort
"""
print("Mapped values are: \n", *map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7]))

print("filter odd  numbers \n", *filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

print("Sorted Key-values are: \n", sorted([('b', 2), ('a', 1), ('c', 3), ('d', 4), ('f', 21)], key=lambda x: x[1]))
