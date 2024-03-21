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
