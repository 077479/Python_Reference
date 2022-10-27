# 7 Decorators
## 7.1 Basics:
- decorators are a design pattern that adds functionality dynamically to an object (decorators adding functionality to a function/method => closure plus)
- a function can be passed as argument to another function to add extra functionality without changing the first function
- it can be imagenend as piped functions => the returnstatement of the one function is the argument of the other and so on. . .
- can be chained up infinite times
- e.g.
```python
def my_decorator(some_function):
    def inner_function():
        some_function()
    return inner_function

@my_decorator
def some_function() # everytime some_function is called the decorators nested function is called
```
- normally a nested function executes the "base" function

## 7.2 Decorator Funnctions With Parameters:
e.g.
```python
def smart_divide(func):
    def inner(a,b):
        if b == 0:
            print("nah i cant")
            return
        else:
            return func(a,b)
    return inner

@smart_divide
def divide(a,b)
    print(a/b)
```
> the usage of "*args"(tuple of arguments = primitive data type) or "**kwargs"(a dictionary of keyword arguments = anything) allows to have any amount of parameters
```python
def star(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args, **kwargs)
        print("*"*30)
    return inner

def diamont(func):
    def inner(*args, **kwargs):
        print("<>"*15)
        func(*args, **kwargs)
        print("<>"*15)
    return inner

@star
@diamont
def printer(msg):
    print(msg)

while True:
    printer(input("say something: "))
```