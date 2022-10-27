# 3 Comprehensions
## 3.1 Basics
- comprehensions are a syntax that allows to filter or transform iterable objects
- often comprehensions are one-liner
- the result can be a list, a dicionary, a Set or a generator (comprehensions are just a conceise tool to create a list,set or dict from a sequence)
- implemented in C => much faster than the for loop
- general syntax: "RETURN_VALUE for ELEMENT in ITERABLE BOOLEAN_LOGIC"
- general syn ex: "x for x in range(21) if x%2==0 and x%5==0" (will return numbers under 21 that are divisorable without rest with 2 and 5)
> please bare in mind that just because you can write functionality in one line, it does not mean it is good practice, oneliner can be fun to make and are a good practice but often they are just bad to read and to maintain

## 3.2 List Comprehensions
- list comprehension processing items in a list, they process every element within the list with a given rule
- used to map input value to output value, applying a filter to include or exclude any values that meet a specific condition
- any iterable can be the input
- the comprehension syntax has to be embedded into "[]" to retrieve a list
- e.g.
```python
matrix = [
        [1.1, 1.2, 1.3],
        [2.1, 2.2, 2.3],
        [3.1, 3.2, 3.3],
            ]
[row[0] for row in matrix] # 1.1, 1.2, 1.3
[col[0] for col in matrix] # 1.1, 2.1, 3.1
```
- the values can be manupilated ''print([row[1] + 7 for row in matrix]) # 9.1, 9.2, 9.3''
- for more complex operations ScyPy or NumPy is used to crunch matrix stored data

## 3.3 Set Comprehensions
- for set comprehension use "{}"
- e.g.
```python
Book = namedtuple("Book", "author title genre")
books = [
        Book("pratchett", "nightwatch", "fantasy"),
        Book("pratchett", "thief of time", "fantasy"),
        Book("le guin", "dispossessed", "scifi"),
        Book("turner", "the thief", "fantasy"),
]
fantasy_authors = {b.author for b in books if b.genre == "fantasy"} # {"turner", "pratchett, le guin"}
```
- elements can only be inserted once in an set, therefor pratchett is only one time in it

## 3.4 Dictionary Comprehensions
- for dict use {key:value}
- e.g.
```python
Book = namedtuple("Book", "author title genre")
books = [
        Book("pratchett", "nightwatch", "fantasy"),
        Book("pratchett", "thief of time", "fantasy"),
        Book("le guin", "dispossessed", "scifi"),
        Book("turner", "the thief", "fantasy"),
]
fantasy_authors = {b.title:b for b in books if b.genre == "fantasy"} # {"turner", "pratchett, le guin"}
```