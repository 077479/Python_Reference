# 2 Iterator Pattern
## 2.1 Basics
- an iterator returns one element of a datastructure after another with a "next" and "done" method
- general implementation could be:
```python
    while not iterator.done()
        item = iterator.next()
        # process item further
```

## 2.2 python implementation:
- in python the iterator is an special object from the collection.abc module (built-in)
- this object demands a ``__next__`` and a ``__iter__`` method
- ``__iter__``: must return an iterator instance that will cover the elements
- ``__next__``: must return the next element, if the iterator instance is exhausted (there are no more elements in it) it has to raise the "StopIteration" exception
- example:
```python
    class CapitalIterable:
        def __init__(self, string):
            self.string = string
        def __iter__(self):
            return CapitalIterator(self.string)
    class CapitalIterator:
        def __init__(self.string):
            self.words = [i.capitalize() for i in string.split()]
            self.index = 0
        def __next__(self):
            if self.index == len(self.words):
                raise StopIteration()
            word = self.words[self.index]
            self.index += 1
            return word
        def __iter__(self):
            return self

    iterable = CapitalIterable("nice little unsuspicious sentence")
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator)) # next is a built-in function
        except StopIteration:
            break
```
- an iterable is an object that can be looped over
- an iterator is a specific instance of the looping, there could be several iterator looping over the same iterable on different positions
- the shortcut for this "iterator instanciating while loop nonsense" is the "for loop" ``for i in iterable:``
