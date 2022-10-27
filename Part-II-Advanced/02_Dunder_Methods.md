# 2 Dunder Methods
## 2.1  Basics
- link to the python doc for dunder methods: https://docs.python.org/3/reference/datamodel.html#special-method-names
- link to an explanation for dunder methods: https://rszalski.github.io/magicmethods/
- link to a list of all dunder methods: https://holycoders.com/python-dunder-special-methods/
- dunder methods are special methods that starts and end with "__"
- they define the "overload" behavior of an object i.e. this methods are called when an object is printed or used with an "*" or "+" operator
- they arent meant to be called directly

## 2.2 example Dunder Methods
- __new__(cls [arg1, arg2, ...]) is called on instance creation (constructor but has almost no usecases)
- __init__(self [arg1, arg2, ...]) is called on instance creation
- __repr__(self) should return a string representation of the class
- __str__(self) called when the "str" or the "print" method is used on the object
- __iter__(self) called in a for loop, has to return an iterable
- __next__(self) called in a for loop, should return one element after another, has to raise StopIteration()
- __add__(self, other) called for the "+" operation
- __enter__(self) called when used with the "with" keyword, to enter the nested codeblock
- __exit__(self) called when used with the "with" keyword, to exit the nested codeblock