# 4 Extending Built-In functions
## 4.1 Basics
- often instead of a new data_type object that has a search or data access method a built_in data structure is inherited and the needed functionality is added
- a class that inherits from a built_in behaves exact the same plus the added functionality
- e.g.
````python
class ContainerList(list):
    # added functionality

my_list = ContainerList()
my_list.append([Element])
element in my_list
````
> commonly extended built_ins are "list, set, dict, file, str" not so common but with usecases are "int, float"

## 4.2 When to Use
- if the usecase is just to store some objects and using the containers features than just create the container as a var within an object, its easy to pass the data structure to a method and to process the content furhter
- however if the usecase is to change the way a container actually works it should be inherited from
- i.e. if a list should store only 5 character long strings, than the "append", ``__setitem__``, "extend" methods must be overwritten
- as a rule of thumb, when u think u are in need of inheriting from a data structure often its better to look which other data structures there are and if they fullfill the need