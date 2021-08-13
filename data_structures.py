"""
This code will contain python data structures

"""
"""Singly linked list
The basic structure of a singly linked list is that it contains:
data
A reference to the next node. Node contains data and the link to the next done.

We will create a singly linked list whose node contains data and the link to the next node
"""


# Define basic element that forms the list
class Node:
    # Constructor for the node (has data and link to next node)
    def __init__(self, data=None, next_node=None):
        self.__data = data
        self.__next_node = next_node

    "define methods to get the data, get next node and set the next node"

    #  Get data
    def get_data(self):
        return self.__data

    # Get the next node
    def get_next(self):
        return self.__next_node

    # Set the next node
    def set_next(self, new_next):
        self.__next_node = new_next


class SinglyLinkedList:
    # Constructor
    def __init__(self):
        self.__head = Node("__head__")

    # Get the first node that contains the specified data
    def get_node(self, data):
        current = self.__head

        # Go through the list until it finds a match, or reach the end of the list
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        return None

    # Delete first node that contains the specified data
    def delete(self, data):
        current = self.__head
        previous = None

        if current.get_data() != data:
            previous = current
            current = current.get_next()
        # Go through the list until it finds a match, or reach the end of the line
        else:
            previous.set_next(current.get_next())
            # break;

    # Append new node to the end of the list
    def append(self, data):
        current = self.__head
        # Go to the last node in the list
        while current.get_next():
            current = current.get_next()

        # Append at the end of the list
        current.set_next(Node(data))

    # Get the number of nodes in the list
    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count - 1

    # Print List
    def print_list(self):
        current = self.__head.get_next()
        while current:
            print(current.get_data)
            current = current.get_next()


"Test our list"
# Create list object
l = SinglyLinkedList()
# Append cat to the list and print
l.append('cat')
# More appends
l.append('dog')
l.append('fish')
l.append('bird')

print(l.print_list())

# Test Get node
node = l.get_node('fish')
print(node.get_data())

# delete fish
l.delete('fish')
print(l.print_list())

# size
print(l.size())