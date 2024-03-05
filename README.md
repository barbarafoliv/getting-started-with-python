# getting-started-with-python
This repository contains my journey through the Advanced Programming with Python course. I’ll be documenting my progress, sharing code snippets, and exploring Python’s powerful features. Let’s dive into the world of Python excellence! 🚀

# Classes and Objects

Objects contain instance variables and instance methods that define their functionalities, which can only be invoked when associated ("self" - the first parameter is the current object).
Classes contain static variables and static methods, invoked by the class itself.

## Visibility of variables:

double underscore __: not visible to other classes or modules
a single underscore _:
no underscore: public

Note: Although it's possible to hide variables, their manipulation by others is always possible.

## Access to variables:

reading - GETTER @property
assignment - SETTER (can include data validation) @Attribute.setter

## Inheritance:
Hierarchy: superclass <- class <- subclass

Note: Python allows multiple inheritance - a class can derive from more than one superclass.