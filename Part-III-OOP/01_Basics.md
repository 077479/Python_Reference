# 1 Basics
## 1.1 Object Orientation
- functionality directed towards modeling objects (one of many modeling techniques to represent complex systems)
- means describing a collection of interacting objects through their data and behaviors

## 1.2 Stages of Softwarte Development
1. Analysis
2. Design
3. Programming
> development happens in iterative development cycles. i.e. a small part of the task is modeled, designed and implemented then reviewed and if neccessary expanded to improve features. this happens in a series of short development cycles

### 1.2.1 Object Oriented Analysis
- the process of identifying objects and interactions between them in a given task(the problem that has to be solved with the application)
- output is a "set of requirements"
- could include:
    - interviewing customers
    - studying their processes
    - eliminating possibilities
> the question in this phase is, what needs to be done

### 1.2.2 Object Oriented Design
- the process of converting the requirements into an implementation specification
- includes:
    - naming objects
    - define the behavior of the objects
    - define which object can trigger behavior on other objects
- the result should be the "implementation specification" (basically a blueprint for the devs, an ideal specification can be implemented in any programmin language)
> the question here is how should it be done

### 1.2.3 Object Oriented Programming
- the process of converting the "implementation specs" into a working application (the actual programming)

## 1.3 Classes
- a class describes a specific object
- they are the blueprints from what the objects are "instanciated"
- the behavior and the data is here defined (but at least the data can be altered after the instanciation)
- one class cna have many instances but not visa vere
> instanciation menas the creation of an object through the class, therefor an object is also called instance of a class (the actual apple would be an instance of the appple class)

## 1.4 Objects
- **Objects**:
    - Objects are models that can do things or have things done to
    - Objectes represent physical objects or abstract ideas in order to model a computer system
    - Objects are instances of classes (there can be many instances with different data of one class e.g. different apple objects with different weight or colors of the class "Apple")
    > def: an Object is a collection of data and associated behaviors

### 1.4.1 Data of an Object
- represents individual characteristics of a certain object
- is defined in the class (means the data attribute is shared by all objects, but the actual value can differ from object to object)
- also callled attribute (e.g. "weight attribute")
- distinction between "property" and "attribute" (i.e. attributes are reffered to as settable and property to as read-only but this distinction is irrelevant in python)
- the type of attributes should be specified (primitives or objects)

### 1.4.2 Behavior of an Object
- actions that can occur on an object
- behavior that can be performed on a specific class of objects is called "method"
- methods can accept parameters and have a return value (like functions)
- parameter are a list of objects that has to be passed (the actual passed parameters are often called arguments)
- return values are the result of the function
> methods are like functions BUT they have access to all the object-specific data

### 1.4.3 Public Interfaces
- interfaces are collections of attributes and methods that other objects can access and interact with
- the idea is that the internal working of an object should be internal => not accessabel for other objects
- an idea behind this is that the implementation can be changed everytime to maintain the code but the public interface can be untouched
- if the public interface is changed every object that access the changed public interface(client objects) has to be changed too!
- the process of hiding the implementation details are called "information hiding"
- a rule of thumb with public interfaces is "to keep it simple"
> design a public interface based on how easy it is to use

### 1.4.4 Encapsulation
- "encapsulation" is a more all encompassing term of "information hiding" (encapsulated data must not be hidden in order to be called encapsulated)
- the distinction of "information hiding" and "encapsulation" is mostly irrelevant for python (in python there is no true information hiding)

# 1.5 Abstraction
- abstraction is the process of encapsulating information with separate public and private interfaces
- only the level of detail that is needed should be used
- think of the distinction of a driver and a mechanic, the driver needs less functionality as a mechanic for a car object

# 1.6 Composition
- the act of collecting several objects together to create a new one 
- i.e. means that one object is part of another 
- e.g. customer object that has an attribute contact which is an own object or a chess set where the chess pieces are separate objects
- proivides levels of abstraction

# 1.7 Aggregation
- a more general form of composition, where aggregated objects can exist independently
- composition is a form of aggregation
- past the design phase the difference if in the mostt cases irrelevant, when implemented they mostly behave the same
> when differentiating between composition and aggregation think about the lifespan(creation, deletion of objects), if the outside object(composite) controls the lifespan of the inner object(related) then it is propably composition if the related object can exist inndependently it is aggregation

# 1.8 Inheritance
- a class can inherit attributes and methods from another class
- the class from where is inherited is called "super class" or "parent class"
- the inheriting class ins called "sub class" or "child class"
- is used in an "is" relationship
- a "ChessPiece" could be a parent class of a "King", the "ChessPiece" would immplement the move function and a color attribute, the king would just inherit these method/attribute and must not implement it
- the idea is that the move method just have to be implemented once for all "chess pieces" like the "bishop", the "knight" even when a new "chess piece" is invented like a "mage" there would not be the concern of movement
- often a dummy method is used when all subclasses have the same method but implement it in different ways (e.g. the "ChessPiece" class whould have a dummy "move" method that the subclasses could implement on its own)
> the implementation of an inherited method is called "override" a subcalss overrides a method from the super class

# 1.9 Abstract Classes
- abstract classes arent mentioned to be instanciated
- an abstract class deinfes a blueprint with abstract methods (abstract methods are methods that must be implemented in a sub class otherwise the interpreter raises an exception, at least in python)
- "abstract classes" can declare an "abstract method" that has to be implemented
- a classe that doesnt implement any methods at all, and just tell what a "sub class" should do, but with no advise on how, are called "interface" (like a skeleton class)
> abstract methods in abstract classes demand that the method exist in any "non-abstract" subclass, but there isnt a default implementation,think of the chess pieces, every chess piece has to move differently

# 1.10 Polymorphism
- the ability to treat a class differently, depending on which subclass is implemented is called polymorphism
- in python referred as "duck typing" (if it walks like a duck or swims like a duck its a duck)
- e.g. a "Penguin" class could implement a "walk" or a "swim" method that could be used by a "DuckFarmer" to treat the penguin like a duck

# 1.11 Multiple Inheritance
- allows a sub class to inherit functionallity from different super classes
- used to create objects with two different sets of behavior (e.g. a printer object merged with a scanner object to create a printer-scanner)
- but gets messy real fast
- the best way to deal with it is to not do it (there are programming languages that prohibits multiple inheritance, java is one of them)
- if it is a solution for a problem go back to design phase and solve it otherwise
> inheritance should be used accordingly in a "something is another thing" relationship, thats the only case when to use inheritance. its like recursion only because you have a hammer not everything is a nail

# 1.12 Suggestions
- sometimes what looks like data is actually calculated from other data in the object
- use different levels of abstraction from high to low in the analysis phase
- look for objects where different approaches could be used and look into how this different approaches would influence the other objects
