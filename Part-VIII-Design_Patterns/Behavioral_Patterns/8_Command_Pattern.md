# 8 Command Pattern
## 8.1 Basics
- provides a layer of abstraction between an action and the invoking of the action
- turns a request into a stand-alone object that contains all information
- lets you pass, delay or queue requests like arguments

## 8.2 Usecase
- everytime the same functionality needs to be implemented into different objects
- e.g. undo actions where a previous state has to be preveiled

## 8.3 General Design
1. sender class initializes a request (must store a reference to the command object)
2. command interface usually executes just a single method for executing the command
3. concrete command implement the various kinds of requests
4. receiver provides teh functionality
5. client creates and configures concrete command objects

## 8.4 Python Implementation
### 8.4.1 Implementation
- in python methods and functions can be passed around
- so instead of creating specialized command objects it might be feasable to just bind the command to an requesting object
- it is also possible to make the command object callable with the ``__call__`` function

### 8.4.2 Example
````python
    import sys

    class Window:
        def exit(self):
            sys.exit(0)
    class MenuItem:
        def click(self):
            self.command()

    window = Window()
    menu_item = MenuItem()
    menu_item.command = window.exit
````