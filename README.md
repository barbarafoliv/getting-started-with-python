# getting-started-with-python
This repository contains my journey through the Advanced Programming with Python course. I’ll document my progress, share code snippets, and explore Python’s powerful features. Let’s dive into the world of Python excellence! 🚀

# Classes and Objects

Objects contain instance variables and methods that define their functionalities, which can only be invoked when associated ("self" - the first parameter is the current object).
Classes contain static variables and static methods, invoked by the class itself.

## Visibility of variables:

double underscore __: PRIVATE - highly encapsulated, not visible to other classes or modules - ex: self.__name
a single underscore _: PROTECTED - attribute should not be accessed outside the class (although it can happen) - ex: self._name
no underscore: PUBLIC - attribute can be accessed from anywhere in code - ex: self.name

Note: Although it's possible to hide variables, their manipulation by others is always possible.

## Access to variables:

reading - GETTER @property - ex: when we write 'person.name', we are calling the method name() defined by the decorator @property
assignment - SETTER (can include data validation) @Attribute.setter

Note: By using Getters and Setters we are following an important programming principle - Encapsulation. This allows the class to control how the attributes are accessed and modified. 

## Inheritance:
Hierarchy: superclass <- class <- subclass

Note: Python allows multiple inheritance - a class can derive from more than one superclass.