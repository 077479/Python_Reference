# 5 Basic Datatypes
## 5.1 list of basic datatypes
>
    |Object Type           | Example                       |
    |----------------------|-------------------------------|
    |Numbers               |int, float, complex            |
    |Strings               |''"pretty string"''            |
    |Lists                 |''[Item1, Item2, ...]''        |
    |Dictionary            |''{key:value}''                |
    |Tuples                |''(item1, item2)''             |
    |Sets                  |''{item1, item2}''             |
    |Files                 |''open("file")''               |		
    |Other                 |Boolean, Types, None           |
    |Program Unit Types    |Module, Class, Function        |
    |Implementation Related|Compiled Code, Stack tracebacks|

## 5.2 Integer
- **Basics**:
    - represents a decimal number without a floating point
    - all integer literals or variables are of the type "int object"
    - leading zeros are not allowed
    - integer are "immutable" (not changeable)
    - as a delimiter for numbers the ''_'' is allowed e.g. ''199_999''
    - integers can be binary, octal, hexadecimal
    - binary: created with ''0b'' or ''0B'' e.g. ''0b1101011'' is 127
    - octal: created with ''0o'' or ''0O'' e.g. ''0o15'' is 15
    - hexadecimal: created with ''0x'' or ''oX'' e.g. ''0xFB'' is 251

- **Operations**:
    >
        | Operation | Description   |
        |-----------|---------------|
        |''+''      |Addition       |
        |''-''      |Subtraction    |
        |''*''      |Multiplication |
        |''/''      |Division       |
        |''%''      |Modulo Division|
        |''**''     |Exponent       |
        |''//''     |Floor Division |

## 5.3 Float
- **Basics**:
    - represent positive and negative "real numbers"
    - the max size depends on the system
    - floats are "immutable"
    - when max/min value is overstepped will return "inf"
    - can be seperated by ''_''
    - denotes by ''.'' or ''e'' or ''E''
    - e.g. ''10.5'', ''1.5e2''(same as 1.5 * 10**2)

- **Operations**:
    >
        | Operation | Description   |
        |-----------|---------------|
        |''+''      |Addition       |
        |''-''      |Subtraction    |
        |''*''      |Multiplication |
        |''/''      |Division       |
        |''%''      |Modulo Division|
        |''**''     |Exponent       |
        |''//''     |Floor Division |

## 5.4 Complex
- **Basics**:
    - represents complex numbers
    - complex are "immutable"
    - e.g. ''x+yj'', where x is the real part and y is the imaginary part (using other symbols will raise an exception)

- **Operations**:
    >
        | Operation | Description   |
        |-----------|---------------|
        |''+''      |Addition       |
        |''-''      |Subtraction    |
        |''*''      |Multiplication |
        |''/''      |Division       |
        |''%''      |Modulo Division|
        |''**''     |Exponent       |
        |''//''     |Floor Division |

## 5.5 Boolean Types
- **Basics**:
    - represent "True" or "False"
    - "True" is also represented by "1"
    - "False" is also represented by "0"
    - a boolean statement evaluation that returns 1 will be considered as True similarly 0 as False
- **Operations**:
    >
        | Operation | Description   |
        |-----------|---------------|
        |''+''      |Addition       |
        |''-''      |Subtraction    |
        |''*''      |Multiplication |
        |''/''      |Division       |
        |''%''      |Modulo Division|
        |''**''     |Exponent       |
        |''//''     |Floor Division |			

## 5.6 String
- link to the python doc for strings: https://docs.python.org/3/library/string.html?highlight=string#module-string
- a string is a sequence of chars
- a "char" is a symbol from an alphabet
- internally chars are represented binary (as a number)
- the used encoding is unicode (can be changed)
- all strings are created from the "string" class
- represented by double ''"'' or double ''"''
- Elements of the string can be accessed via "indexing" or "slicing"

## 5.7 Primitive Data Type Methods
- int(): returns an int object
- float(): returns a float object
- str(): returns a string object
- complex(): returns a complex number
- hex(): converts an int into a hexadecimal number with prefix 0x
- oct(): converts an int into a octal number with prefix 0o
- pow(): returns the power of an int
- abs(): returns the absolute value of an int (the value of the number without -/+)
- round(): returns the rounded number