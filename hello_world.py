# simple hello world printouts


print('Hello world')
print("Hello world")

print("""


Hello 

world""")
"""
# Comments

# Python interpreter ignores comments.

# Use triple quotes to input comments in multiple lines
"""

"""
# Variables:
Containers to store values
variable names cannot be python keywords\
Use print("keywords") to view all the keywords in the current python module
Don't Start variable with a digit

"""
a = 1
print("The value of a is:", a)

"""
Exchange values of variables
"""
b = 2
print("The current Values of a is", a, "and the current value of b is", b)

# Exchange the values of A and B
a, b = b, a
print("The new Values of a is", a, 'and the new value of b is', b)

"""
Global and Local Variables
Global: declared with global scope (code block without indentation)
Local: Declared with local scope (code block with indentation)
"""
a = 1  # Global variable


def func():  # define a function
    f = 2  # Local variable


c = 3

print('The summation of the global variables is', a + c)
# f can only be accessed within the code block.

# print('This summation will cause an error "f is not defined"', a + f)

"""
Standard input output

Uncomment the code below and run
"""
# s = input("Input the number you want to print: ")
# print(s)

"""
Python functions

A function is a block of reusable code which can be invoked by calling
"""
