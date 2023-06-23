# This example demonstrates polymorphism in Python.

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

    def get_name(self):
        return super().get_name() + " (Employee)"
    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.__email = email

    def get_name(self):
        return super().get_name() + " (Customer)"
    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

def get_name(obj):
    return obj.get_name()

e = Employee("John", 10000)
c = Customer("Jack", "abc@somedomain.com")

print(get_name(e))
print(e.get_salary())

print(get_name(c))
print(c.get_email())

# Output:
# John (Employee)
# 10000

# Jack (Customer)
# abc@somedomain.com

# The Employee class and the Customer class both inherit from the Person class.
# The get_name() and set_name() methods of the Person class are available to both the Employee class and the Customer class.
# The Employee class has its own get_salary() and set_salary() methods.
# The Customer class has its own get_email() and set_email() methods.
# This is called polymorphism.