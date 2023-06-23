# This example demonstrates encapsulation in Python.
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("John")
print(p.get_name())
p.set_name("Jack")
print(p.get_name())

# Output:
# John
# Jack

# The __name attribute is private to the class and cannot be accessed from outside the class.
# The get_name() and set_name() methods are used to access and modify the __name attribute.
# This is called encapsulation.