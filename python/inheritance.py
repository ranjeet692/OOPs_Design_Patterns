# This example demonstrates inheritance in Python.

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

e = Employee("John", 10000)

print(e.get_name())
print(e.get_salary())

# Output:
# John
# 10000

# The Employee class inherits from the Person class.
# The __init__() method of the Employee class calls the __init__() method of the Person class using super().
# The get_name() and set_name() methods of the Person class are available to the Employee class.
# The Employee class also has its own get_salary() and set_salary() methods.
# This is called inheritance.