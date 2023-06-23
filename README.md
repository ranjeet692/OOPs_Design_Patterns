# OOPs & Design Patterns

## OOPs

**Object-Oriented Programming (OOP)** is a powerful programming language model that emphasizes the use of objects and their interactions to design applications. It is a popular programming paradigm because it provides a clean and organized way of coding. OOP is based on a set of principles that include encapsulation, inheritance, and polymorphism. These principles enable developers to build complex software systems that are easier to maintain and modify.

### Encapsulation

**Encapsulation** is a crucial principle in Object-Oriented Programming (OOP) that involves bundling data and methods within a single unit, known as a class. This simplifies the code and ensures that data is not modified in unexpected ways. Access modifiers (public, private, and protected) control the access level of other classes to the data within a class. Encapsulation is necessary because it hides class implementation details from other classes and makes code more secure by preventing unauthorized access to data. In short, encapsulation is a vital OOP principle that bundles data and methods, controls access, and prevents bugs and security issues.

### Inheritance

**Inheritance** is another crucial principle in OOP that involves creating a new class based on an existing class. The new class inherits the properties and methods of the existing class, making it easier to reuse code and create new classes quickly. Inheritance is useful because it allows developers to create new classes that are similar to existing classes but with slightly different functionality. This can save time and effort when developing software systems that require similar classes with different functionality.

### Polymorphism

**Polymorphism** is an essential principle in OOP that allows objects of different classes to be treated as if they were objects of the same class. This means that objects can be passed as arguments to methods that expect different classes of objects, allowing for more flexible and scalable code. Polymorphism is achieved through method overloading and method overriding. Method overloading involves creating multiple methods with the same name but different parameters, while method overriding involves creating a new implementation of a method in a subclass. Polymorphism is useful because it allows developers to write code that is more flexible and can handle a wider range of situations.

## Design Patterns

Design patterns are used to solve common problems that arise in software development. In OOP, design patterns help developers build software systems that are modular, reusable, and scalable. There are many design patterns available in OOP, but in this project, we will focus the three most common OOP design patterns.

### Singleton Pattern

The Singleton pattern is a creational pattern that restricts the instantiation of a class to one object. This pattern is useful when we need to ensure that only one instance of a class exists in the entire application. This can be useful when we need to limit access to a shared resource, such as a database connection. The Singleton pattern is implemented by creating a static instance of the class and ensuring that all instances of the class reference this static instance.

### Factory Pattern

The Factory pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This provides a way to create objects without specifying the exact class of object that will be created. The Factory pattern is useful when we need to create objects that are related but may differ in their implementation. This pattern allows for more flexibility and scalability in object creation.

### Observer Pattern

The Observer pattern is a behavioral pattern that allows an object to notify other objects of changes to its state. This pattern is useful when we need to maintain consistency between related objects. In the Observer pattern, an object maintains a list of dependent objects and notifies them automatically of any state changes. This allows the dependent objects to update their state to match the state of the original object. This pattern is commonly used in graphical user interfaces, where changes to one part of the interface need to be reflected in other parts.
