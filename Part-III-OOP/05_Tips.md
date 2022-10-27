# 5 Tips
## 5.1 Overloading
- in python when an object offers a specific method it can be used with built-in functions or operators like it is another data type (e.g. if an object provides the ``__add__`` method it can be used with the "+" operator)
- used to extend the functionality of objects to be used by built-in functions, but is not restricted to that

## 5.2 Monkey Patching
- replacing or adding methods at runtime is called monkeypatching
````python
class A:
    def print(self):
        print("Iam in class A")

def fake_print():
    print("iam clearly not in class A muhahahahahaha")

a = A()
a.print = fake_print
````
- even class methods can be exchanged (then the "self" keyword has to be in the given arguments) but after that the method changes for all objects even for the instanciated ones
- is used to fix bugs or to add functionality to third-party code or to adapt an existing library to suit the usecase
- should be used sparingly is considered a "messy hack"

## 5.3 Callable Objects
- the magic method "__call__" sets the behavior when an object is called
- e.g.
````python
class A:
    def __call__(self):
        print("interesting")
a = A()
a()
````
- the idea is that an instanciated object is callable
- if its not an instanciated object that has to be called its 90% of the time the wrong solution (not the right abstraction)