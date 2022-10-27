# 7 Datatstructures
## 7.1 List
- **Basics**:
    - lists are positional ordered collections of items
    - elements are separated by ``,``
    - no fixed type constraint (means items within a list can be from different types)
    - lists are mutable
    - lists are a flexible tool to represent data
    - items are accessed via "Indexing" or "Slicing"
    - indexing out of the boundary raises an exception

- **Operators**:
    >
        |Operator  |Description                                                      |
        |----------|-----------------------------------------------------------------|
        |``+``     |concatinates two lists (adds them together)                      |
        |``*``     |concatenates multiple copies of the same list (multiplies them)  |
        |``in``    |returns "True" if a given pattern is content of the list         |
        |``not in``|returns "False" if the given pattern is content of the list      |

- **Methods**:
    - ``list.index(Object, start, end)`` returns the index(ordered position) of the object. can have optional arguments that determining a section of the content to search
    - ``list.extend(IterableObject)`` adds the items in the given object to the list (modifies the original list)
    - ``list.append("Object")`` adds the object at the end of the list
    - ``list.insert(INDEX, Object)`` inserts an object at the given index
    - ``list.remove(Object)`` removes the object from the list
    - ``list.count(Object)`` returns an int that represents the amount of occurances of the object within the list
    - ``list.pop(INDEX=-1)`` removes the last item from the list and returns it
    - ``list.reverse()`` reverses the order of the list. DOES not return anything
    - ``list.sort(key , reverse=True/False)`` sorts the items in the list, if a key is given it sorts after a specific order
    - ``list.copy()`` returns a copy of the list // assigning a new var to a list is not copying
    - ``list.clear()`` removes all items from the list
    - ``list.sort()``:
        - sort is a function of the list object that sorts the content of the list
        - without parameters it will sort in ascending order alphabetically (uppercase first)
        - if the content is unsortable an error will be raised
        - an object needs to define the "__lt__" (lower than) method in order to be considered sortable

- **Nesting**:
    - lists can be nested unlimited, list in a list in a list
    - used to describe multidimensional array (matrix)
    - but should be used wisely, if deeper than 2 levels there are other ways provided by the 3rd party package **NumPy**

- **When to Use**:
    - when several instances of the same type of object has to be stored
    - when to elements should be stored in some kind of order
    - when the stored objects has to be changed
    - DONT use lists to store different attributes of individual items

## 7.2 Tuples
- **Basics**:
    - tuples are "immutable"(unchangeable) lists
    - createb by ``(item1, item2, ...)`` or packing ``my_pretty_tuple = 1,3,"dogsname"``
    - if an item in a tuple is a data structure that is "mutabel" items in that can be changed
    - cant be created with only one item
    - can be accessed via "indexing" or "slicing"
    - can be unpacked => ``a,b,c = (1,2,3)`` (the tuple content is stored in the variables a,b,c)

- **Operations**:
    - ``+`` returns a new tuple with the content of the added tuple
    - ``*`` concatenates multiple copies of the tuple
    - ``in`` returns True if the item is an element of the tuple
    - ``not in`` returns True if the item is not an element of the tuple

- **Methods**:
    - ``tuple.count(Object)`` will return an int that represent the number of occurances of the object in the tuple
    - ``tuple.index(Object)`` will return an int that represent the index of the object in the tuple

- **When to use a tuple over a list**:
    - a tuple is only suitable when the content of the tuple is clear and when it is unpacked and not just one or two items are needed here and there (if used that way, make at least a comment where the var is coming from and what it represents) // use tuples only when you know that all vars going to be useful at once to prevent "magic" numbers to pop up and nobody knows where that comes from
    - iterating over a tuple is much faster
    - with immutabel elements it can be used as key for dictionaries

## 7.3 Named Tuples
- the named tuple is a specialised form of the tuple from the "collections" module (built-in)
- named tuples are tuples with attitude
- used when it is known in advance which attributes has to be stored
- used when the stored data is not in need of behavior
- used to group "read only" data together
- constructed with ``namedtuple("Identifier", list of string attributes that is required by the named tuple)``
- construction example
```python
from collections import namedtuple

pc = namedtuple("player_char", ["name", "age class race"])
pc_1 = pc("Hendrik", 57, class="Mage", race="Elf") 

# just for the sake of showing the assignment of named arguments, all given arguments can be named, but the order will also set them to the correct argument
```
- can be accessed like a normal tuple or like an object => ``pc_1.name``

# 7.4 Dataclass
- dataclasses are regular objects with a clean way to predefine attributes
- dataclasses are in the "dataclasses" module (is a built-in)
- dataclasses using a lower amount of memory as normal objects, so when handling a large number of objects this might be an alternative
> another alternative could be **slots**
- there are different ways to construct a dataclass
- the "make_dataclass" function in the module dataclasses or the "dataclass object" itself
- e.g.
```python
from dataclass import make_dataclass, dataclass

# make dataclass
pc = make_dataclass("name", "age", "class")

# wrapper
@dataclass
class Pc:
    name: str
    age: int
    class: str
```
- dataclass supports equality comparision (the content of the vars are tested for equality, all have to be the same)
- with the "order=True" modifier greater or lesser comparisions are supported
- e.g. ``@dataclass(order=True)``
- **DATA CLASSES ARE NOT ITERABLE** if this is needed and a dataclass has to be used create a custom dataclass

## 7.5 Set
- **Basic**:
    - a set is an unordered collection of hashable objects that does not allow double elements
    - the items must be immutable // python hashes the objects and the hash changes when the content of an object change
    - is created by ``{item1, item2, ...}`` or ``set()``
    - a set is mutable
    - often used for mathematical operations like union or intersection(Mengenoperationen)
    - the items can be different types
    - the items in a set are inherently unordered
    - purpose is to divide the world in items in the set and others
- **Methods**:
    - ``set.add(Object)`` adds a single element to the set
    - ``set.update(Object)`` adds a group of elements to a set, can be a data structure // can be added to all of the following statements to update the current set e.g. set.union(set2).update()
    - ``set.discard(Object)`` removes an item from the set, wont raise an exception if the object doesnt exist
    - ``set.remove(Object)`` removes an item from the set will raise an exception when the elemetn doesnt exist
    - ``set.pop(Object)`` will remove a random element of the set and returns it (will get the last one but a set is unordered)
    - ``set.clear(Object)`` will remove all items from the set
    - ``set.copy(Object)`` returns a shallow copy of the set
    - ``set.union(set2)`` or ``set1 | set2`` will return the union(vereinigungsmenge) of two sets
    - ``set.intersection(set2)`` or ``set1 & set2`` will return the intersection(schnittmengen) of two sets
    - ``set.isdisjoint(set2)`` return true if the sets have no intersections
    - ``set.difference(set2)`` or ``set1 - set2`` will return a set without the elements that are also in the second set
    - ``set.symmetric_difference(Object)`` or ``set2 ^ set2`` intersection reversed
    - ``set.issubset(Object)`` returns true if another set contains this set
    - ``set.superset(Object)`` returns true if this set contains another set

## 7.6 Frozenset
    - frozen sets are immutable sets => means the set itself can be hashed
    - its created by the method ``frozenset(ITERABLE)``

## 7.7 Dictionaries
- **Basics**:
    - dictionaries are associative data structures => key-value pairs
    - dictionaries are ordered collections(returning the items will be ordered) of key value pairs // berefore 3.7 they we unordered!
    - created by ``pretty_dict = {key1:value1, key2:value2, ...}`` or by the ``dict()`` method
    - values can be of any type and can repeat
    - keys must be unique and imutable with immutable elements(if a data structure) // string, numeric, frozenset, tuple
    - values are accessed by the key e.g. ``pretty_dict["key1"]``
    - values can be edited or added by the ``=`` operator e.g. ``pretty_dict["key1"] = "pretty new value"``
- **Operations**:
    - ``Object in dict`` returns "True" if the object is a key in the dictionary
    - ``Object not in dict`` returns "False" if the object is a key in the dictionary
- **Methods**:
    - ``dict.clear()`` removes all items
    - ``dict.copy()`` returns a shallow copy of the dict
    - ``dict.fromkeys(ITERABLE WITH KEYS)`` returns a dict with the elements of the given keys
    - ``dict.get(KEY)`` returns the value, returns None if the value does not exist
    - ``dict.items()`` returns the "key:value" pairs as dict_item objects
    - ``dict.keys()`` returns the keys from the dict
    - ``dict.pop(KEY)`` removes and returns the value
    - ``dict.popitem()`` removes and returns the last "key:value" pair (before python 3.7 it was random)
    - ``dict.setdefault(KEY, VALUE)`` returns a value by the given key, if the key doesnt exist it will be created with the given value
    - ``dict.update()`` updates the dict with key/value pairs of another dictionary, existing pairs will be overwritten
    - ``dict.values()`` returns all values
- **Comprehensions**:
    - can create a dictionary from any "iterable" source through a lambda
    - e.g. ``square = {x: x*x for x in range(6)}`` creates a dict with the numbers 0 to 5 as keys and the squares as value
- **When to Use**:
    - everytime you want to find an object based on some other object
    - if you want to group certain data together and dont know exactly how much data or which data will be stored

## 7.8 Defaultdict
- a defaultdict is a specialised form of dict from the "collections" module (built-in)
- a defaultdict behaves like a dict, but that everytime a key is not in the dict it will be created
- the constructor of a defaultdict accepts a function, if a key is not in the dicionaty it calls the funtion
- e.g.
```python
from collections import defaultdict # import defaultdict
def letter_amount(sentence): # function that accept a string representing a sentence
    amount = defaultdict(int) # setting the defaultdict and pass the int func to it (will create an int with the value 0)
    for letter in sentence: # iterate over the string char by char
        amount[letter] = +1 # access the defaultdict and set the value
    return amount # return the defaultdict
```
- a use case could be: to create a dictionary of closing stock prices for 30 days, the stock name of a company could be used as key (as str) and the function could be the "list" function, everytime a stock name is not in the dict it will create a empty list linked to the stock name as key

## 7.9 Counter
- a class for the usecase of counting specific instances in an iterable
- part of the "colletions" module (built-in)
- behaves like a dictionary where the key items being counted and the values are the quantities of them
- e.g.
```python
from collections import Counter
def letter_frequency(sentence):
    return Counter(sentence)
```

## 7.10 Casting/Conversion
- **Basics**:
    - the process of converting a data type to another is called "casting" or "conversion"
    - in python there are built in functions to cast/convert datatypes
    - int(), float(), str()
    - when not convertable-data is converted an exception is raised // e.g. int("two")
- **Implicit**:
    - automatic conversion by the python interpreter is called implicit casting
    - e.g. ``num = 123`` auto create an int
    - auto conversion will use the larger type to prevent a loss of precision
    - has its limitations, will raise an exception if not sure which datatype to use (often when trying to concenate numeric and strings)
- **Explicit**:
    - also called "Typecasting", the user casts a new type to an object
    - done by using the data type methods like ``int()`` or ``str()``