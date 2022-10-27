# 6 String and Serilization
## 6.1 Strings
- link to the string doc: https://docs.python.org/3/library/string.html?highlight=string#module-string
- strings are primitive objects in python
- constructed with "str()" or just double ''"'' or double ''"''
- they represent an immutable sequence of unicode chars
- link to a unicode table: https://www.ssec.wisc.edu/~tomw/java/unicode.html

## 6.2 String Manipulation
- strings can be concatenated (added together with the "+" operator)
- strings can be accessed with "sequence operations"
- strings can be iterated over (the iter object then yields the unicode chars)
- the string object comes with some convinience functionality
    - ``isalpha/isupper/islower``: pretty obvious
    - ``startswidth/ednswidth``: pretty obvious
    - ``count``: returns how often a (str)pattern is part of the string
    - ``find/index/rfind/rindex``: returning the index of the first match (find returns "-1" if the pattern isnt found, index will raise an error)
    - ``upper/lower/capitalize/title``: obvious
    - ``replace``: obvious
    - ``split``: obvious
    - ``isspace``: obvious, BUT consider tab and newline are considered whitespace chars
    - ``istitle``: returns True if all words are beginning with a capitalized letter
    - ``isdigit/isdecimal/isnumeric``: obvious, but does not recognize "." as a number, but other unicode chars are considered a number
- The gist of that should be consider that the standard boolean checks arent that great
- note that the most if not all of the methods dont change the string itself, they just return a new string therefor a often used idion is ``pretty_str = pretty_str.title()``
- if a method is not obvious to you just use the help function on it ``help("".split)``

## 6.3 String Formatting
### 6.3.1 F-String
- the preffered method of formatting is the "format string" or "f-string"
- if a "f" is right infront of the string it is considered a "f-string"
- in a f-string the logic(in a moderate way) can be placed within ``{}`` these brackets
- complex objects (lists, tuples, dictionaries, arbitrary objects) can be used in f-strings (can be accessed like a normal object)
- variables from the surrounding namespace can be inserted too
- e.g. ``f"the result of 3**452 is {3**452}"`` or ``f"Hello {name} how is your {activity}"``
- the gist here is every object that provides the ``__str__`` method (has to return a string) can be used within the brackets
- double brackets escape the brackets => ``f"here are the double brackets {{}}"``
- alternatively use a ``\`` to escape any char

## 6.3.2 Older String formatting the format method
- format method is an object from the class string
- in the format method no function can be called
- integers can map the placeholders
- it uses ``{}`` as placeholder for statements
- the statement can be a keyword, a number, a function call or nothing(then the sequence counts)
- an even older format-option uses ``%``as placeholder
- e.g. ``"the result of 3**-452 is {}".format(3**-452)`` or ``"Hello {} how is your {}".format(name, activity)``

## 6.3.3 Specifier for the Format String Arguments
- the output of the logic within a f-string can be specified with arguments
- these arguments are stated together with the object after a ``:``
- example: ``f"this is my byte {my_byte:00>8b}"``
- **char**:
    - the char will be added as leading value if the given length isnt reached (often used for binary representation)
    - e.g. ``f"{my_byte:0>8b}"`` will display the binary number in 8bit parts normally leading zeros would be cut off but the argument prevents that
- **</^/>**: the alignment - left, justify/center, justify/right/
- **value**: how much space should be reserverd for the placeholder
- **b**: binary displaying (numerics only)
- **e**: scientific displaying (numerics only)
- **value.decimal_spaces**: specification of the number of decimal places
- **f**: means float (accepts argue for the number of decimal places after the comma => n.mf)
- **d**: means int
- e.g. ``f"here is it just cut to 2 decimals after the point {3**-452:10.2f}"``
- all these format options are ordered and cant be mixed up, however they can be left out
- custom formatters can be implemented with the ``__format__`` interface

## 6.4 Strings, Ascii and Unicode
- unicode is a map that maps all existing symbols that there are in the world to a number
- the map of unicode has 2**21 places (around 2million), not all of them are assigned
- ascii is a map that maps the normal used symbols of the latin language plus a few extras (2**7 places, the eight byte is reserved for extra characters)
- the mapping of ascii corresponds to the unicode mapping (makes ascii a subset of unicode)
- typically not the whole unicode map is used therefore there are maps that differ in its capaity (UTF-8, UTF-16, UTF-32)
- information stored on a computer is stored as 8bit chunks (called byte)
- so the unicode or ascii "encoding" looks at the 8bit chunks and assigns the mapping to the ordinal number that is represented by the 8bit chunks => 01100001 = 0x61 = 97 = the encodin of the char "a"
- there are several different "encodings" like stated before normally used are "UTF-8" or "UTF-16" but there are many others like "latin-1"
- if the right encoding is not used the information stored cant be restored
- the used encoding differs from os to os and from regional setting to regional setting
- python provides the ``sys.getdefaultencoding()`` function to get the default encoding used by the os
- when handling string serilization it is best to provide the specific encodings (the software might run in another part of the world or on otehr systems)
- when in doubt the ``utf-8`` encoding should be choosen, is kind of the todays standard

## 6.5 Bytes and Text
### 6.5.1 byte to text
- in python bytes are represented by the byte class
- a byte class can be created like a string but infront of the string a "b" or "B" has to be put followed by the hexadecimal numbers, a "\x" seperates the hexadecimal numbers
- the byte class has the methode "decode()"
- the "decode()" method accepts a "encoding format" lite "utf-8" or "latin-1" or "ascii"
- e.g.
```python
chars = b"\x63\x6c\x69\x63\x68\xe9" # creates the byte object and fills it with data
chars.decode("latin-1") # decodes teh byte chunk with the latin-1 mapping
chars.decode("utf-16") # decodes the byte chunk with the utf-16 mapping
chars.decode("iso8859-5") # decodes teh chunk with the cyrillic mapping
```

## 6.5.2 text to byte
- the string class has the method "encode"
- e.g.
```python
chars = "cliché"
chars.encode("utf-1")
chars.encode("latin-1")
chars.encode("cp437")
```
- the encode method accepts a furhter argument that determines how to process in the encoding unknown elements
- arguments of the encode method
    - **replace**: replaces the char with a "?"(for ascii), 
    - **ignore**: removes the char
    - **xmlcharrefreplace**: replaces the char with the xml version (needed for work with xml files)

## 6.5.3 bytearray
- to store multiple byte objects python provides a specialized list for bytes the "bytearray"