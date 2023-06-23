# This example demonstrates factory design pattern in Python.

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

class PersonFactory:
    @staticmethod
    def create_person(type):
        if type == "employee":
            return Employee("John", 10000)
        elif type == "customer":
            return Customer("Jack", "abc@somedomain.com")
        else:
            return Person("")
        
p1 = PersonFactory.create_person("employee")
print(p1.get_name())

p2 = PersonFactory.create_person("customer")
print(p2.get_name())

p3 = PersonFactory.create_person("guest")
print(p3.get_name())

# Output:
# John (Employee)
# Jack (Customer)
#   

# The PersonFactory class is a factory class that creates objects of the Person class and its subclasses.
# The create_person() method of the PersonFactory class creates and returns objects of the Person class and its subclasses.
# The create_person() method takes a type parameter and returns an object of the Person class or its subclasses based on the type parameter.
# The create_person() method returns an object of the Person class if the type parameter is not "employee" or "customer".
# The create_person() method returns an object of the Employee class if the type parameter is "employee".
# The create_person() method returns an object of the Customer class if the type parameter is "customer".

# The factory design pattern is used to create objects of a class without exposing the creation logic to the client.
# The factory design pattern is used when we have a super class with multiple sub-classes and based on input, we need to return one of the sub-class.

# This example demonstrates factory design pattern in Python.