# This example demostrate observer design pattern in Python.

class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notify_all('notification')

# Output:
# Observer1 :: Got ('notification',) From <__main__.Subject object at 0x7f9d38033d00>
# Observer2 :: Got ('notification',) From <__main__.Subject object at 0x7f9d38033d00>

# The Subject class has a private attribute __observers which is a list of Observer objects.
# The register() method is used to add an observer to the list.
# The notify_all() method is used to notify all the observers in the list.
# The Observer1 and Observer2 classes are observers.
# The Observer1 and Observer2 classes have a notify() method which is called when the Subject class calls the notify_all() method.
# This is called observer design pattern.