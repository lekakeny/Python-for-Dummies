""""
OOP organizes sw design around objects and not functions and logic.

Much more readable and understandable

Object: collection of data (variables) and methods (functions) that act on that data

Object is a blueprint for an object

Object is an instance of a class

Features of OOP
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism - object can have many forms

"""

"Create a class that stimulates a dog"


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def run(self):
        print(self.name.title() + " is now running")


"Instantiation"
the_dog = Dog('Simba', 4)
the_dog.sit()
the_dog.run()

"Adding new data to the object"
the_dog.food = 'cat food'
print("The dog's food is", the_dog.food)

"We can redefine a class"


class Dog(object):
    def __init__(self, name):
        self.name = name
        print("%s has been created" % self.name)


the_dog = Dog('Chui')

"Implementing the string method customizes the expected printout"


class Dog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The name of the dog is: " + self.name


the_dog = Dog('Chui')
print(the_dog)

"""
Encapsulation
Private and public methods and data is used to implement encapsulation. 

A private method and data is created by adding double underscore in front of it. 

Private methods and data can only be accessed from inside the object

"""


class SimpleCounter():
    __secretCount = 0  # private variable
    publicCount = 0  # private variable

    def count(self):
        self.__secretCount += 100
        self.publicCount += 150
        print("This is the private count: ", self.__secretCount)


counter = SimpleCounter()
counter.count()
print("This is the public count: ", counter.publicCount)

"Trying to access private methods from outside the object will result to an error"
# print(counter.__secretCount)  # Cannot access private variables directly from outside the object.
"AttributeError: 'SimpleCounter' object has no attribute '__secretCount'"

"""
Inheritance

Allows us to define a class that inherits all the data and methods from the parent class

"""


class parent:  # This is the parent class
    parentAttribute = 100

    def __init__(self):
        print("Instantiating the Parent Class")

    def parentMethod(self):
        print("This is how the parent treats the child (method)")

    def setAttribute(self, attr):
        parent.parentAttribute = attr

    def getAttribute(self):
        print("Parent Attribute: ", parent.parentAttribute)


class child(parent):  # This is the child class, it inherits the data and attributes of the parent class above
    def __init__(self):
        print("Instantiating the child")

    def childMethod(self):
        print("This is how the child behaves (method)")

    def getAttribute(self):
        super().getAttribute()
        print("Child says hello mama")


# Instantiating the class child
toto = child()  # Instantiate the child
toto.childMethod()  # Call the child method
toto.parentMethod()  # Call the parent Method
toto.setAttribute(821)  # set attribute (parent method)
toto.getAttribute()  # Call attribute (parent method)

"""
If we define data and methods in child class that are already defined in parent class, then the data and methods 
in child class will override those of the parent class in the child class
"""

"We can also add new data  and methods to child"
toto.childMethod()  # call childMethod

"""
Abstraction

An abstract class is a blueprint of other classes

An animal is an abstract of a cow.

Abstraction is meant to hide details from the users

ABC module is used to define base abstract classes in python

Any class that inherits from an abstract class will be required to override the abstract method in the parent class
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def lays_eggs(self):
        pass

    @abstractmethod
    def eats_grass(self):
        pass

    def is_an_animal(self):
        return True


class Cow(Animal):
    def __init__(self):
        print("Sema Ng'ombe")

    # overriding abstract method (This is required)
    def eats_grass(self):
        return True

    def lays_eggs(self):
        print("Kuadimika kama nayai ya ng'ombe")
        return False


moo = Cow()
print("A cow is an animal: ", moo.is_an_animal())
print("A cow eats grass: %s" % moo.eats_grass())
print("A cow lays eggs", moo.lays_eggs())

"""
Polymorphism

Ability of an object to have many forms
"""

"The function len can return the length of a string or a list"

print("The length of this string is: ", len("Ole Karoi"))
print("The length of the provided list is: ", len([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

"Polymorphism with classes and inheritance"


class Animal:
    def sound(self):
        pass


class cat(Animal):
    def sound(self):
        print("I don't know why people like cats. Maybe its because of its sound miew~~")


class dog(Animal):
    def sound(self):
        print("The dog Barks so loudly, my daughter gets scared everytime it barks")


class fish(Animal):
    def sound(self):
        print("I don't know the sound of fish")

# In this case cow is not morphing from animal (not inheriting either)
class cow:
    def sound(self):
        print("The cow says mooh!")


kitty = cat()
katty = dog()
jelly = fish()
sambu = cow()

my_animals = [kitty, katty, jelly, sambu]

for instance in my_animals:
    instance.sound()


"Verify if the animals are types of animal"

"Kitty is a cat and is also an animal"
print(isinstance(kitty, cat))
print(isinstance(kitty, Animal))

"My cow is not an animal! Only on my code. The real cow looks like an animal"
print(isinstance(sambu, cow))
print(isinstance(sambu, Animal))

"Great! Now I have an idea of basic Python. I will now do a test for basic python"