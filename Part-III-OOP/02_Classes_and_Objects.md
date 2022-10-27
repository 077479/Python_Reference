# 2 Classes and Objects
## 2.1 Classes
- classes are defined by the keyword "class" followed by the name of the class "Name"
- remember the naming convention

## 2.2 Class Attributes
- a class attribute is an attribute that is bound to the class
- all instances of this class can access and share this attribute (a change will lead to a change for all instances)
- is accessed by "object.classattribute_name" or "Class.classattribute_name"

## 2.3 Class Methods
- class methods are similar to the class attributes shared by all instances, it is created by the "@classmethod" decorator and the first parameter has to be "cls" instead of self
- accessed by "object.classmethod_name()" or "class.classmethod_name()"
> be aware that instancename.classattribute = value will lead to the creation of a new attribute in the namespace!

## 2.4 Static Methods
- is a classmmethod that knows nothing about the class
- is bound to the class
- is mostly used as an utility method that doesnt need any attributes of the class, but where it makes sense to bind the functionality to the class
- cant have "cls" or "self" as attribute (therefore cant access attributes of the class or the object)
- called with ''Class.Method()'' or ''Object.Method()''
- is assigned through the "static method" decorator ''@staticmethod''

## 2.5 Object Attributes
- attributes/methods can be accessed through the dot notation "Object.Attribute"
- see also property decorators

## 2.6 Object Methods
- methods are declared like functions through the "def" keyword
- can have parameters
- return value is determined through the "return" keyword if not given the default return value is "None"
- default values can be assigned same with normal python functions

## 2.7 Self
- a methods first parameter must be a reference to the object itself, usually done by passing "self" as argument but could be named anything
- when calling the same method on different objects the same method is called but different objects are passed
- is a easy way to invoke the function on the class
- python intern happens:
````python
p = Point() # an instance of Point is created and referenced by the var p
Point.reset(p) # the method reset of the point class is called and the instance p is given as parameter
````

## 2.8 Constructor/Initializer
- the constructor function is ``__new__`` But in python the constructor is rarely til never used
- to set the initial status of an object the ``__init__`` method is used
- ``__init__`` can be used like any other mehtod

## 2.9 Modules
- modules are simply the files with the extension ''.py''
- every item from the namespace of a module can be imported (or the whole module)

## 2.10 Packages
- a package is a collection of modules (just a dir with python files)
- in order to be recognised as package the directory has to contain an "init.py" file
- can have subfolders (must have also an init.py file)
- accessible through the "dot" notation e.g. package.subfolder.module.class.classmethod()
- the init.py file is the logistic of a package, but dont put too much logic into it no one will expect this and there will be "where the heck is this name coming from" moments

## 2.11 init.py
- the ``__init__.py`` file tells the interpreter that a directory contains code for a python module
- without the "init" you cant import modulles from another folder(including subfolders)
- role is similar to a "constructor", its the "constructor" for the package
- is used to tell the interpreter what modules should be aviable when the package is imported
- can be empty(then all modules are aviable)
- example init file
- ``__all__`` all statement refers to the modules that should be imported when the "wild card" import statement is used ``from PACKAGE import *`` e.g. ``__all__ = [LIST, OF, MODULES, FOR, THE, WILD]``
- But dont put too much logic into it no one will expect this and there will be "where the heck is this name coming from" moments

## 2.12 Access Control
- Normallly programming languages have something like this:
    - as private marked attributes are only accessale through the object itself
    - as protected marked attributes are only accessable through the class and subclasses
    - as public marked attributes can be accessed by any other object
- Python doesnt do this
- in python all attributes of a class are aviable
- but internal attributes/functionality should be named with an underscore ``_`` infornt of the name (is kind of equivalent of protected BUT it is aviable from any objects its just the naming shows other devs that this is functionality that shouldnt be accessed)
- to name mangle an attribute the name of an attribute/functionality has to start with double underscores ``__`` (its kind of equivalent of private BUT it is aviable from the outside but other devs will see that this really shouldnt be touched) 
> name mangling means that the propertie is prefixed with ``_<classname>_`` but it has rare usecases

## 2.13 Class Property
- to encapsulate an attribute from the outside getter and setter are used
- getter and setter are methods to make sure that attributes of an object are correct used. the attribute shouldnt be called directly and should be accessed via setter/getter
- in python this is realized through class properties, they provide an interface for the attributes
- so even if an Object calls the attribute by the name with the ''.'' operator the getter/setter method will be called
- the idea is to not use getter/setter and only if u are in need of access control a setter can be implemented (at any point in time, because of teh property object functionality the public api to the property will be the same)
- python provides three properties for that plus the doc
    - ''fget'' function for getting the attribute
    - ''fset'' function for setting the attribute
    - ''fdel'' function for deleting the attribute val
    - ''doc'' a string that contains the documentation
- to assign an property to the attribute the "property function" has to be called ''name_of_attribute = property(get_attr, set_attr, del_attr, doc="brief description")''
- e.g.
````python
class Person():
    def __init__(self, arg_name):
        self.name = arg_name

    def get_name(self):
        print("in the getter")
        return name

    def set_name(self, arg_name):
        print("in the setter")
        self.name = arg_name

    def del_name(self):
        print("in the delete function")
        del self.name

    name = property(get_name, set_name, del_name, doc="name of person")

jerry = Person("jerry")
jerry.name # will call the getter
jerry.name = hans # will call the setter
````

## 2.14 Property Decorators
- the getter/setter can be created without "linking" them to the attribute with the property asssignnment function, instead decorators can be used
- a decorator is the operator ''@'' and the decoratorname e.g. "setter" => ''@attr_name.setter''
- there are three property decorator
- ''@property'' assignes an attr_name to the property (works as getter)
- ''@property_method_name.setter'' defines the setter method for the attribute
- ''@property_method_name.deleter'' defines the del method handling
- the actual name of the property and the name of the object attribute doesnt have to be the same e.g. the example object attribute is called "_name" the property is called "name"
- e.g.
````python
class Person():
    def __init__(self, arg_name):
        self._name = arg_name # could use the private naming for the attribute (self.__name = arg_name) then the private naming for this attribute has to be used in the whole class

    @property # property decorator(i.e. getter) is applied to the name() method
    def name(self):
        print("in the getter")
        return name

    @name.setter
    def name(self, arg_name):
        print("in the setter")
        self.name = arg_name

    @name.deleter
    def name(self):
        print("in the delete function")
        del self.name

jerry = Person("jerry")
jerry.name # will call the getter
jerry.name = hans # will call the setter
````