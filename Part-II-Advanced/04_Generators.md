# 4 Generators
## 4.1 basics
- gernerators are a specialized form of comprehensions
- is a shortcut to create a kind of object
- the key to generators is the ``yield`` keyword
- the ``yield`` statement works like a return, but instead of exiting the iterable object, it will continue the "yielding" of elements after processing of said element, one at a time
- for that python wraps an iterable into a special generator object that does this magic
- the generator object has a ``__iter__`` and a ``__next__`` method, when the next method is called it returns the next item and saves the state and suspends, til the next "next" call

## 4.2 Sum
- the gernerator works like the "list comprehension" but instead of returning a list of processed elements it will return one processed object after another (runs the function til a "yield" is encountered, returns the value and pauses teh function til the next "next" call)
- a function with the "yield" statement returns an iterator object
- is created through a yield statement instead of a return statement
- the yield statement pauses the function, saves the state and suspend the function and the calling object has the process
- returns an iterator object, but does not start it
- the iterator protocoll is implemented automatically
- when the generator function terminates it raises the "StopIteration" exception
- can be used in arguments for functions without paranthesis
- is memory friendly because only one item at the time will be processed
- represent an infinite stream of data (cant be stored because its infinite)
- is ideal for pipelining (a yielded value can be processed by another generator)
- can be used in a for loop

## 4.3 example
```python
def pow(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
gen__ob = pow(3)
next(gen_obj) # 1
next(gen_obj) # 2
next(gen_obj) # 4

class File:
    def __init__(self, name):
        self.name = name

class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.children = list()

root = Folder("")
etc = Folder("etc")
var = Folder("var")

root.children.append(etc)
root.children.append(var)

etc.children.append(Folder("httpd"))
etc.children.append(File("passwd"))
etc.children.append(File("groups"))

httpd.children.append(File("http.conf"))

log = Folder("log")
var.children.append(log)

log.children.append(File("messages"))
log.children.append(File("kernel"))

def walk(file):
    if isinstance(file, Folder):
        yield file.name + "/"
        for f in file.children:
            yield from walk(f)
    else:
        yield file.name
```