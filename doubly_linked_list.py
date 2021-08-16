"""
For a doubly linked list, we add a reference to the previous node in a singly linked list

"""


# Define the basic elements that forms the list
class Node:
    # Constructor
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.__data = data
        self.__next_node = next_node
        self.__prev_node = prev_node

    # Define Methods to get data, get next node, set next node and set previous node
    # get data
    def get_data(self):
        return self.__data

    # Get next node
    def get_next(self):
        return self.__next_node

    # Set next node
    def set_next(self, new_next):
        self.__next_node = new_next

    # Get Previous Node
    def get_prev(self):
        return self.__prev_node

    # Set previous node
    def set_prev(self, new_prev):
        self.__prev_node = new_prev


"Define the list"


class DoublyLinkedList:

    # Constructor
    def __init__(self):
        head = Node('__head__')
        self.__head = head
        self.__tail = head

    # Get the first node that contains the specified data
    def get_node(self, data):
        current = self.__head

        # Go through the list until it finds a match, or reach the end of the list
        while current:
            if current.get_data() == data:
                return current
            else:
                current.get_next()
        return None

    # Append new node to the end of the list
    def append(self, data):
        new_tail = Node(data)
        self.__tail.set_next(new_tail)
        new_tail.set_prev(self.__tail)
        self.__tail = new_tail

    # Delete first node that contains specified data
    def delete(self, data):
        del_node = self.get_node(data)
        if del_node:
            prev_node = del_node.get_prev()
            next_node = del_node.get_next()
            prev_node.set_next(next_node)
            if next_node:
                next_node.set_next(prev_node)
            else:
                self.__tail = prev_node

    # Get the number of nodes in the list
    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count - 1

    # Print list
    def print_list(self):
        current = self.__head.get_next()
        while current:
            print(current.get_data())
            current = current.get_next()

    # Print Backwards for Double Linked List
    def print_backwards(self):
        current = self.__tail
        while current.get_prev():
            print(current.get_data())
            current = current.get_prev()


"Test our list"
# Create list object
l = DoublyLinkedList()
# Append cat to the list and print
l.append('cat')
# More appends
l.append('dog')
l.append('fish')
l.append('bird')
print("This is the Forward list")
l.print_list()

# Print Backwards
print("This is the backwards list")
l.print_backwards()

# Delete "Cat"
l.delete("cat")
print("This is the list after deleting Cat")
l.print_list()

# Let's see the size of the list
print("The size of the list is %d" % l.size())
# l.size()

# # Test Get node
# node = l.get_node('fish')
# print(node.get_data())
#
# # delete fish
# l.delete('fish')
# print(l.print_list())
#
# # size
# print(l.size())
