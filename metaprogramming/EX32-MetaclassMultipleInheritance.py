class MetaClass(type):
    """Example of constructing a metaclass"""
    def __new__(cls, class_name, superclasses, attribute_dict):
        return super(MetaClass, cls).__new__(cls, class_name, superclasses, attribute_dict)

## The class of type MetaClass
A = MetaClass('A', (object, ), {})

print('Type of class A:', type(A))

class B(object):
    pass

print('Type of class B:', type(B))

## Class C inherits from both classes, A and B
class C(A, B):
    pass

print('Type of class C:', type(C))
