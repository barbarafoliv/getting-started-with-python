# Getting Started with Python

Welcome to my repository! This is where I document my journey through the Advanced Programming with Python course. I’ll be sharing my progress, code snippets, and the exploration of Python’s powerful features. Let's dive into the world of Python excellence! 🚀

## Classes and Objects

In Python, objects contain instance variables and methods that define their functionalities. These can only be invoked when associated with the object itself (referred to as "self"). On the other hand, classes contain static variables and static methods, which are invoked by the class itself.

### Visibility of Variables

- **Private** (`__`): These are highly encapsulated variables that are not visible to other classes or modules. For example, `self.__name`.
- **Protected** (`_`): These attributes should not be accessed outside the class, although it can happen. For example, `self._name`.
- **Public**: These attributes can be accessed from anywhere in the code. For example, `self.name`.

> Note: Although it's possible to hide variables, their manipulation by others is always possible.

### Access to Variables

- **Getter** (`@property`): This is used for reading the variable. For example, when we write 'person.name', we are calling the method `name()` defined by the decorator `@property`.
- **Setter** (`@Attribute.setter`): This is used for assigning values to the variable. It can include data validation.

> Note: By using Getters and Setters we are following an important programming principle - Encapsulation. This allows the class to control how the attributes are accessed and modified.

## Inheritance

Inheritance in Python follows a hierarchy: `superclass <- class <- subclass`. Python also allows multiple inheritance, which means a class can derive from more than one superclass.

## Metaprogramming in Python

### Metaclasses

Metaclasses are classes that create other classes. They allow you to customize how classes are created, adding specific behaviors or validating the structure of the class before its creation. To define a metaclass, you create a class that inherits from `type` and define a special method: `__new__` or `__init__`.

### Type

Example:
```python
LanguageType = type('LanguageType', (object, ), {
    '__init__': init,
    'getLanguage': getLanguage,
})
```

In the type method, there are three arguments:

- The string 'LanguageType' is the name of the class.
- The tuple (object, ) indicates that this class inherits from the object class. The comma at the end helps the Python interpreter recognize it as a tuple.
- The dictionary specifies the attributes and methods of the class. In this case, it contains two methods: init and getLanguage.

Metaclasses implement the __new__ method, which takes four arguments:
1. The metaclass itself.
2. The name of the class.
3. The superclasses, in the form of a tuple.
4. The attributes of the class, in the form of a dictionary.

> Note: Metaclasses in Python are classes that define the behavior of other classes. Python doesn't allow multiple inheritance from metaclasses, just from one. 

## Iterators and Coroutines

Iterators are methods that allow iterating collections of data such as lists, tuples, etc. It allows traversing an object and returning its elements. The Python iterator object must implement the `__iter__()` and `__next__()` methods - Iterator Protocol.

### Properties of iterators

- The iteration object remembers the iteration count through the internal count variable.
- Once the iteration is complete, it raises a `StopIteration` exception, and the iteration count cannot be reset to 0.
- Therefore, it can be used to traverse the content only once.

## Django

Django is a Python framework that makes it easier to create web sites using Python. 
Django is especially helpful for database driven websites.

### MVT Design Pattern

Django follows the MVT design pattern (Model View Template).

- Model - The data you want to present, usually data from a database.
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

### Virtual Environment

It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

### Django Views

Django views are Python functions that takes http requests and returns http response, like HTML documents.
A web page that uses Django is full of views with different tasks and missions.

> Note: The name of the view does not have to be the same as the application.

### SQLite Database

When we created the Django project, we got an empty SQLite database. By default, all Models created in the Django project will be created as tables in this database.

### Django QuerySet

A QuerySet is a collection of data from a database that is built up as a list of objects.
QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.