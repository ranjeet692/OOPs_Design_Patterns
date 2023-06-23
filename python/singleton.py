# This example demonstrates singleton design pattern in Python.

class Singleton:
    __instance = None

    @staticmethod 
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

a = Singleton()
print(a)

b = Singleton.get_instance()
print(b)

c = Singleton.get_instance()
print(c)

# Output:
# <__main__.Singleton object at 0x7f9d38033bb0>
# <__main__.Singleton object at 0x7f9d38033bb0>
# <__main__.Singleton object at 0x7f9d38033bb0>

# The Singleton class has a private static attribute __instance.
# The get_instance() method returns the __instance attribute.
# The __init__() method is called only once when the __instance attribute is None.
# This is called singleton design pattern.