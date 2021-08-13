"""
Generators are functions that return a lazy iterator
lazy iterators do not store their contents in memory, unlike lists
generators generate elements/values when you iterate over it
It is lazy because it will not calculate the element until when we want to use the element
"""
"Use isinstance function to check if an object is iterable"
import collections as c

print(isinstance([], c.Iterable))
print(isinstance('a,b,c', c.Iterable))
print(isinstance(100, c.Iterable))
print(isinstance((1, 2, 3, 4, 5, 6,), c.Iterable))

"Create an iterator using iter function"
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
l_iteration = iter(l)
print("The type of iterator is: ", type(l_iteration))

"The next function provides the next element in the iterator"
print("First Value is: ", next(l_iteration))
print("Second Value is: ", next(l_iteration))
print("Third Value is: ", next(l_iteration))
print("Fourth Value is: ", next(l_iteration))

# Generators: We define how each element in the iterator is generated
"Use the example of n fibonacci numbers to learn the generators"

print("fibonacci begins here")


def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num2
        num1, num2 = num2, num1 + num2
        current += 1
        yield num  # We use key word yield instead of return when building a generator
    yield "Done"


g = fib(5)
for number in g:
    print(number)

"A shorter way to create generators is using list comprehensions"

g = (x ** 2 for x in range(5))
print("This has been done using list comprehension")
for x in g:
    print(x)
"""
Decorators
Add functionality to an existing code without modifying its structure
It is a function that returns another function. Callable object that returns another callable object
Takes in a function, add some functionality and returns it
Provides a flexible way of adding/extending the functionality of a function
"""


def decorate(decorated_function):
    def decorated():
        print("This is the decorated function")
        decorated_function()

    return decorated()


@decorate
def plain():
    print("I am not decorated at all!")


plain()
