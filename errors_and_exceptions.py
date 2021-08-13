"""
Errors stop a program from being excecuted

Syntax/parsing errors: when the syntax of the language is not followed. Its the grammar of the code

Exceptions: Errors detected during execution. eg 1/0

We handle exception errors by try-except statements
"""

"This is a syntax error!"  # I mean remove the quotes and run the code

"Python cannot compute 1/0"
# print(1 / 0)  # This is an exception error

"Handle Exceptions using try-except statements, Dan says Try-Catch"
try:
    print(1 / 0)
except Exception as exception_error:
    print(exception_error)
finally:
    print("Python works either way")

"Another Try-Except Error statement handling"
a = 'a'
try:
    b = [value for value in range(int(a))]
    print(b[5] / 0)  # The first error is possible when a<6
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("ValueError")
except IndexError:
    print("List Index out of range")
finally:
    print("Python has no issue with the code")

"Customizing Exceptions by inheriting Exception Class"


class My_Error(Exception):
    def __init__(self, Error_info):
        super().__init__(self)  # initialize parent class
        self.error_info = Error_info

    def __str__(self):
        return self.error_info


# # Throw and exception
# raise My_Error("My custom Exception")

"""Assert Statement: used to evaluate the logical truth of a statement. usually used to test the logical correctness 
of a code 
"""


def assert_function(a, b):
    # if not a==b, python will raise an error
    assert a == b


assert_function(1, 2)
