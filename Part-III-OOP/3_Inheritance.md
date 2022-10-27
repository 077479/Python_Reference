# 3 Inheritance
## 3.1 Superclass
- a "Superclass" also called "Parentclass" is the class thats data/behavior is inherited from
- description

## 3.2 Subclass
- a "Subclass" also called "Childclass" is the class that inherits data/behavior from the "Superclass"
- in python to inherit from a class the name of the "superclass" has to be given as argument in the class definition
- e.g ''class subclass_name(superclass_name)''

## 3.3 Overriding
- overriding means altering or replacing a method from the "Superclass", with the same name within the subclass
- there is no special syntax, just call the overriden method
- any method can be overriden

## 3.4 Super
- sometimes it is necessary to trigger behavior of the "Superclass", a common use case is overriding the ``__init__`` method, often in order to provide the functionality of the "Superclass" the original initialisation is needed
- to realise that the "super" keyword is used
- e.g.
````python
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Phonecontact(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
````
- a super call can be made from everywhere within the class
- it doesnt need to be the first statement within a codeblock

## 3.5 Multiple Inheritance
- in python an object can inherit from more than one "Superclass"
- simplest version is a "mixin" i.e. superclass that is not intended to exist on its own, rahter to be inherited to add functionality to a class. a class called "MailSender" could have the only purpose to provide "email sending" functionality so a "MailableContact" class could be mixed together by inheriting from MailSender class and Contact class
- AS A RULE OF THUMB "if u think u need multiple inheritance you are probably wrong, but if u know you need it you could be right"
- there are programming languages that forbid this completly like "java"
- good alternatives to multiple inheritance:
    - add the needed functionality to on of the classes and inherit from there
    - create a standalone function for one of the needed functionality and just use this
    - use composition instead e.g. add an email object with the email functionality(send/receive) and add it to the contact class rather than create a contact email hybrid
    - monkey patch the functionality

## 3.6 Polymorphism
- the concept of triggering different behaviors with the same interface
> think of an AudioPlayer class that accepts a FileClass that has a play method. Each fileformat would have an own class in which the different play methods are implemented (a mp3 must be decoded in another way as an ogg file). Every object with a "play method" could be used by the AudioPlayer class
- an example is the built_in python operator +, used on an "int object" it does the mathematical operation, used on a str it concatenates the strings or the keyword "in"
- every class could implement the interface to work with an "if" keyword (dunder methods)
- so every object that supply the correct interface can be used interchangeably, in pyton
- it goes even further, not even the complete interface of an object has to be provided, the object only must fullfill the interface that is actually acessed
- i.e. in order to be played by an audio recorder a object must not provide the whole functionality of an audio file, only the play functionality (in a manner that the audio player understand it)

## 3.7 Abstract Base Class (ABC)
- abcs define a set of methods and properties that a class must implement in order to be considered a "duck type" instance of an "abc" (abstract base class) class
- abstract classes arent meant to be instanciated, they only provide a "roadmap" for subclasses
- an abstract class can mark a method as "abstract method" in order to force the subclasses that are meant to be instanciated to implemennt this method
- if a class implements the abstract methods of an "abc" class it is considered a subclass of the "abc" even if it doesnt inherit from the "abc" 
> Duck typing, it moves like a duck so it is a duck, this works with the classmethod ``__subclasshook__``
- the "ABC" class from the "abc" module is used to provide interfaces through the "@abstractmethod" or the "@abstractproperty"
- e.g.
````python
from abc import ABC, abstrctmethod

class my_interface(ABC):
    @abstractproperty
    def age(self):
        pass
    @abstractmethod
    def do_abstract_functionality(self):
        pass
# the my_interface class cant be instanciated without providing the method and the property(variable)
````