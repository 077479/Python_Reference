# 1 Functions to Know
## 1.1 map()
- the map function applies a function to every element of an iterable and yields the result
- often used with lambdas
- ``map(function, iterable)`` returns a map object
    1. "function" the function that is used on each element
    2. "iterable" one or more iterable objects
- e.g. 
```python
for i in map(lambda x:x*x, range(6)):
    print(i)
```

## 1.2 filter()
- the filter function applies a "boolean statement" to every element in an iterable and returns a bool(True/False)
- often used with lambdas
- ``filter(function, iterable)``
- ``filter(lambda x:x%2==0, range(7))`` returns all even numbers

## 1.3 reduce()
- the reduce function processes all elementsof an iterable object
- it takes a function that needs 2 arguments
- it uses the first two elements of the iterable as arguments for the function
- then it uses the result as first argument of the function and the nexe element as the second, and so it runs through all elements of the iterable
- often used with lambdas
- ``reduce(function, iterable)``
- ``reduce(lambda x,y:x*y, range(8))``

## 1.4 range()
- range function generates a list of numbers
- ``range(start, stop, step)`` stop/step is optional
- ``range(0, 8, 1)`` generates a list with the numbers 0 to 7
- the last value wont be generated
- can be used to generate a standard "for loop"

## 1.5 assert()
- evaluates a "boolean statement"
- if the result is "True" the execution will go on
- if not it raises an AssertError
- ``assert(boolean statement, "ErrorMessage")``
- used in testing

## 1.6 len()
- returns the amount of items in a collection
- internally calls Obj.__len__(obj)

## 1.7 reversed()
- takes any sequence as input and returns a copy of it in reversed order
- used in for loops when in need of loop over items from back to front
- internally calls the __reversed__ function on the class ``Obj.__reversed__(obj)``

## 1.8 enumerate()
- iterates over a container, it creates a sequence of tuples where the first element represents the index (starting at 0)
- and the second element the item 

## 1.9 all()
- checks if all items in an iterable are True
- ``all([True, True, False])`` or ``all([0,0,1])``

## 1.10 eval, exec, compile
- executing code that are given as string
- BE CAREFUL tehy are not safe! all unknown users are malacious, foolish, or both

## 1.11 zip()
- takes two or more sequences and returns a new sequences of tuples
- each tuple contains the next element of the originally given containers
