# 1.1 Namingconvention
## Purpose of material
<table>
<tr> <th></th> <th>Studying</th> <th>Coding</th></tr>
<tr> <th>practice</th> <th>tutorials</th> <th>how to guides</th></tr>
<tr> <th>theory</th> <th>explanation</th> <th>references</th></tr>
</table>

## Basics
- link to the Naming Convention Pep: https://www.python.org/dev/peps/pep-0008/
- Python is *case-sensitive* => test, Test, teSt are three different thingis

## general rules
- allowed is a combination of *lowercase*(a-z), *uppercase*(A-Z), *numbers*(0-9), *underscore*(_)
- a name cannot start with a number
- python keywords cant be used as names
- the name should make sense

## for Classes
- the first letter should be Uppercase
- the CamelCase notation should be used (different words arent seperated but are indicated through a uppercase Letter)
- e.g. `BoldMaker`

## for Functions
- name should be complete in lowercase
- different words should be separated by `_`
- name should be a verb
- e.g. `make_bold`

## for Variables
- the name should be all in lowercase
- different words should be separated by `_`
- name should be a noun
- e.g. `legal_age`

## for Constants
- name should be complete in uppercase
- name should be a noun

## for Modules/Packages
- name should be complete in lowercase
- multiple words should be separated by `_`
- e.g. `converter_script`



# 1.2 Codeblocks and Indentations
- in python codeblocks are indicated by the indentation (same indentation = same codeblock)
- as indentation can be used tabs or whitespaces (4 Whitespaces are preferred)
- the number of indentations can freely be choosen, but has to be coherent within a codeblock (it makes sense to choose a style and to stick to it)
- it is common to use 4 whitespaces instead of tabs
- in line continuations the indentation can be ignored, but should also be used
- incorrect indentation will raise an *IndentationError*



# 1.3 Conceptual Hierarchy
## Basic
- *Programs* are composed of *Modules*
- *Modules* are composed of *Statements*
- *Statements* are composed of *Expressions*
- *Expressions* create and process *Objects*

## Program
- collection of modules(can also just be one module or script) to solve a task

## Module
- just a file with the ending *.py*

## Statements
- a statement is an instruction that the interpreter can use
- statements are ending with the end of the line (means each line is a statement)
- statements can be *force* spanned over multiple lines with `\`
- multiple statements can be separated in one line with `;`
- expressions in `( )`, `[ ]`, `{ }` can naturally be spread over multiple lines (means without the use of `\`)



# 1.4 Scripts Explanation
- whan a program gets larger it makes sense to use a file as input for the code. this file is called *script*
- a *script* is a program that solves a specific problem without creating a complex structure of code. it wouldnt make sense to import a script in order to use functions or other parts of it in another program
- scripts that are *importable* in order to use certain functionality in the main



# 1.5 Built-In Functionality/Keywords
- link to the python doc for the builtins: https://docs.python.org/3/library/functions.html
- python provides keywords, builtin objects/functions(functions are objects too in python), and operators, that, together with the right syntax(putting them in the correct order), are forming the statements
- they are just functions/modules provided by python itself
- a list of the keywords can be found direct in python in a module called keyword
- a list of the built-in objects can be foud in the module builtins
```python
    import keyword, builtins # import statement for the builtins and keyword module
    for i in keyword.kwlist: # iterating over the content
        print(i) # outputting the content
    for i in dir(builtins):
        print(i)
```



# 1.6 Comments
## basics
- a comment is a part of a file that is ignored by the python interpreter

## line comments
- `#` to start a comment
- extends til new line

## multiline comments
- `'''` or `"""` to start or end a multiline comment
- mainly used for docstrings



# 1.7 Operators
- operators are special symbols that carry out operations
- the value that the operator operates on is called operand
<table>
<tr> <th>Operator</th>      <th>Name</th>           <th>Description</th> </tr>
<tr> <th>Arithmetic</th>    <th></th>               <th></th> </tr>
<tr> <td>+</td>             <td>addition</td>       <td>adds two operands together</td> </tr>
<tr> <td>-</td>             <td>subtract</td>       <td>subtracts two operands from another</td> </tr>
<tr> <td>*</td>             <td>multipliton</td>    <td>multiplys the operands</td> </tr>
<tr> <td>/</td>             <td>division</td>       <td>divides left operand by the right one (result is always float)</td> </tr>
<tr> <td>%</td>             <td>modulo</td>         <td>returns the remainder of a division</td> </tr>
<tr> <td>//</td>            <td>floor division</td> <td>returns a division result as int (casting is done after the operation is finished, just cuts the comma)</td> </tr>
<tr> <td>**</td>            <td>exponent</td>       <td>left operand is raised to the power of right</td> </tr>

<tr> <th>Comparsion</th>    <th></th>                       <th></th> </tr>
<tr> <td>></td>             <td>is greater</td>             <td>returns bool</td> </tr>
<tr> <td>>=</td>            <td>equals or is greater</td>   <td>returns bool</td> </tr>
<tr> <td><</td>             <td>is lesser</td>              <td>returns bool</td> </tr>
<tr> <td><=</td>            <td>equals or is lesser</td>    <td>returns bool</td> </tr>
<tr> <td>==</td>            <td>equals</td>                 <td>returns bool</td> </tr>
<tr> <td>!=</td>            <td>equals not</td>             <td>returns bool</td> </tr>

<tr> <th>Logical</th>       <th></th>               <th></th> </tr>
<tr> <td>and</td>           <td>logical and</td>    <td>-</td> </tr>
<tr> <td>or</td>            <td>logical or</td>     <td>-</td> </tr>
<tr> <td>not</td>           <td>logical not</td>    <td>-</td> </tr>

<tr> <th>Membership</th>    <th></th>   <th></th> </tr>
<tr> <td>in</td>            <td>-</td>  <td>returns True if an object is in an iterable object</td> </tr>
<tr> <td>not in</td>        <td>-</td>  <td>returns False if an object is in an iterable object</td> </tr>

<tr> <th>identify</th>      <th></th>   <th></th> </tr>
<tr> <td>is</td>            <td>-</td>  <td>returns True if the operand refer to the same object</td> </tr>
<tr> <td>is not</td>        <td>-</td>  <td>returns True if the operand does not refer to the same object</td> </tr>
</table>



# 1.8 Variables
- a variable is a named location to store data
- declaration and assigning a variable is one step ( a = 5 is legit, no need for a = int; a = 5 (like in java))
- a value is assigned to a var *assigning* operator `=`
- multiple assignments in one statement are legit `a, b, c = 10, *hello*, [1,2]` (a = 10, b = 20 will raise an error)



# 1.9 Constants
- constants are variables which content cant be changed
- should be written in uppercase `LEGIT_AGE`
- the interpreter dont prevent constants from beeing overwritten, so the value can actually be changed



# 1.10 Print/Input
## Print
- `print()` is a python built-in function that outputs text to stdout(most times the console)
- `print(*objects, sep=* *, end=*\n*, file=sys.stdout, flush=False)`
    - **objects**: data to be outputted
    - **sep**: seperator to use between values
    - **end**: printed after the data is printed (default is the new-line char)
    - **file**: where to print
- the preferred way to format a string is the fstring(introduced in python 3.6)
- the text within the curvey brackets will be evaluated and accordingly outputted
- to mark a string as *fstring* a f has to be putted infront

```python
    # example fstring
    text = pretty
    f"iam a '{text}' string" # output would be "iam a 'pretty' string"
```

- before that the format method was the preffered way
```python
    # example format method
    *the value is {}*.format(1.2)
    *i love {0} and {1}*.format(*bread*, *butter*) # will result in *i love bread and butter*
    *i love {1} and {0}*.format(*bread*, *butter*) # will result in *i love butter and bread*
    *hello {name}*.format(name=*Sir John*)
    x = 3.1415
    *value is %3.2f* # will result in *value is 3.14*
    *value is %3.4f* # will result in *value is 3.1415*
```

## Input:
- `input()` awaits shell input from the user
    - e.g. `input([*text*])`
    - text will be prompted then the console will halt and wait for input(return key)
- `eval()` same as *input* but evaluates the user input
    - e.g. `eval(2+3)`
    - (be aware that an eval statement can be misused)



# 1.11 Sequence Operations
## Basics
- sequential data types like lists store data in a order, the order is created through indexes where the index 0 is the first stored data!
- indexes are coded offsets from the front, beginning with 0
- to access a stored item the index has to be given `my_list[INDEX]`
- to access a entire section slicing can be used
- in the moment it is ok if it doesnt make sense, but when we discuss data structures you will see it again and then have a *ah sure i heard of that* moment (atleast that the intent here)

## Indexing
- to access data stored in such a data type the index has to be adressed through `[INDEX]`
- the index can be negative, then it will be counted from the end to the start, beginning with -1 as the last item stored
- e.g.: `important_list[0,1,2,3,LAST]`, `important_list[-4,-3,-2,-1]`

## Slicing:
- to extract entire sections from an indexable object (returns only the items, does not access them) a section can be given to the data structure
- does not change the data, just returns it
- e.g.: `my_important_list[start:end:step]` the default is [0:len(obj):1] (len() is a built-in function that returns the length of an iterable object like a list)
    - **start**: sets the start point for the section
    - **end**: sets the endpoint of the section
    - **step**: sets the increment rate  (1 for every, 2 for every second and so on)



# 1.12 Namespace
## Basics
- names are identifyers that we give data structures to acces the underlying objects `age = 5 # an integer object is stored in the memory, the name to access this object is *age*`
- a namespace is a collection of names (a mapping of all vars that are accessible)
- when the python interpreter is started a namespace is created and all the built-ins are added to it
- each module creates his own global namespace
- different namespaces can coexist but are isolated from each other, so the same name for an object in different modules/local namespaces within a module will not collide
- the function `globals()` will return a dictionary with all vars that are aviable in the calling namespace
- when a function is called a local namespace is created(means objects and values outside of the function arent accessable without giving it to the function) 

> a Modul has a global namespace, a function a local namespace

- the isolation of the namespaces is managed through scopes // a scope is the range of a calling object
- 3 namespaces are aviable everytime:
    - scope of the current function
    - scope of the module
    - outermost scope(the one with the built-ins)
- when a reference is made inside a function, the order of searched namespaces is:
    - local namespace
    - global namespace
    - built-in namespace
- in a nested function (function in a function) the inner function has its own namespace
- within a function the global and built-in namespaces are aviable BUT every var not in the local namespace of the function is read-only aviable (i.e. global vars are callable BUT a try to assign a new value to the global var it has to made aviable with the keyword global within the namespace! otherwise a new var is created within the actual namespace with the same name)
- from the *lower* namespace to the *higher* vars only can be read, creating or accessing a var with the same name will result in the creation of a complete new var within the local namespace
- the keyword `global` will make a var from the *global namespace* accessable (writable)
- the keyword `nonlocal` will make a var from the next outer namespace accessible (writable)

## Global Variables Across Modules
- to create Objects/Data Structures that are acessible across multiple/all modules within a project they should be stored in a seperated module normally called *config.py*
- to access and change data in the config.py there should be a seperated module normally called *update.py*
```python
# content of *config.py*
age = 18

# content of *update.py*
age = 19

# content of *main.py*
import config, update
print(config.age) # will return 19 because when importing a script the content will run exactly (this can be triggered again) once so be aware of that!
```



# 1.13 Mutable/Immutable
## Immutabel
- immutabel objects can not be altered once assigned/created
- some immutable objects are:
    - number
    - string
    - tuple
## Mutable
- mutable objects can be altered, it is possible to add, delete, insert, rearrange items
- some mutable objects are:
    - list
    - set
    - dictionary
- now you will say one moment pal, i can change the content of a string, but ehhh not exactly, the interpreter creates a new var with the same name and new content



# 1.14 Import/PythonPath/Reload
## Definitions
- **module**
    - every file with a ``.py`` extension is considered a module
- **package**
    - every directory with python files in it is considered a package (since 3.3)
    - there is a distinction between namespace packages and regular packages
    - before pythin 3.3 only directoies with an ``__init__.py`` file were considered a python package
    - in python 3.3 were namespace packages added (directories without an ``__init__.py file)
    - this feature were added to hndle packages that are distributet over different locations on python_path as one package
    - explanation: [link](https://stackoverflow.com/questions/21819649/namespace-vs-regular-package)
- **absolute import**
    - import specifies the ressource to be imported using its full path from the project root
    - are preferred because clearer to read/understand where a statement comes from
    - stay valid even if the import location changes
- **relative import**
    - import specifies the ressource to be imported using the path relative of the location of the file
    - reducing long import statements
    - in python 3 relative import statements are restricted
- **pythonpath**
    - the *PYTHONPATH* is a *environmentvariable* where the location for python packages/modules is stored (for built_ins and third party)
- **sys.path**
    - at program start initialised list of locations to search for packages/modules
    - can be accessed with ``import sys; sys.path``
    - the directory from where the python file is started is added as teh first entry of this list!
- symbols to represent a tree structure: ├ ─ ┼│└

## Basics
- link to further informations how the import mechanics work: [link](https://fortierq.github.io/python-import/). [link](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
- the import suggestion are stated in PEP 8
    - the importstatement should come after the module docstring
    - the importstatement should be divided into three groups:
        1. python built-in modules
        2. modules that are 3rd party and do not belog to the actual application
        3. modules that belong to the current application => local imports
- there are two different ways to import, "*relative*" and "*absolute*" imports
- absolute imports are preferred!
- an import statement runs the imported module one time! every not nested code is executed

### __init__ file
- before python 3.6 each folder in order to be recodnised as *package* has to have a `__init__.py` file
- this file is run when the package is imported, the namespace here is added
- used to gather package wide elements
- can be considered as the constructor of the package
- if you want to access python files in sub-directories as if they were in the native namespace, it has to be imported in the ``__init__.py`` of the package

## Import:
- ``import module/package``: 
    - creates a reference to the module in the current namespace
    - access with the complete modul path => ``import foo; foo.bar()`` imports foo, accesses bar in the foo module
- ``from module/package import module/object``
    - creates a reference to all members listed after import
    - creates no reference to the module/package!
    - access with the path to the reference => ``from foo import bar; bar()`` import bar from foo NOT foo
- ``import destination as reference_name`` => gives the reference an alias
- ``from package/module import destination as reference_name`` => gives the reference an alias

## order of python imports
- the way python searches for the to be imported element is:
    1. built_ins
    2. pythonpath
    3. sys.path

## Reload:
- after an import statement the imported Object wil be processed exactly once, this means that all code that there is will be processed, in the most cases it wont trigger anything but be aware that an imported script is processed, this means that all initializing of the script that isnt nested in a function will be processed! // therefor a script should be started with an evaluation that indicates that the script were run by the interpreter directly => if __name__ == *__main__*:
- means when there are vars that are set by execution they are set for the runtime of the interpreter they dont change no matter how often the import statement is repeated(import runs the imported source exactly one time!)
- with the command `reload(Object)` from the *importlib* module, the imported object can be loaded again (a while ago it was the imp module but thats depricated and will be removed in version 3.12 of python)

## import examples
- example structure:
>
    [] project root
    │
    ├── []app
    │   ├── __init__.py
    │   ├── fct_1
    │   └── fct_2
    │   
    ├── []tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── test_app.py
    │
    └── run.py

## show importable element in location
```python
import pkgutil
search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
```


# 1.15 Additional Informations
## import this:
- try the command `import this` to get an essay about the idea of python

## id(OBJECT):
- returns the id of a specific object, the id is bound to the memory allocation and will change with a change of the value. // different variables assigned to the same object will have the same id!

## type(OBJECT):
- returns the class of the object

## isinstance(OBJECT):
- checks if an object belongs to a specific class

## sys.version_info:
- returns the python version

## sys.platform:
- returns the os

## Main Method
- `__name__`
    - returns the name of the attribute(not only module, can also be used for a name of a function)
- `__main__`
    - the file that starts the program (the executed script) gets `__main__` as the name attribute this can be a pythonian way of a main method
    - when a script is imported functions are only executed when called
    - code that dont has to be called is executed right away for example to set an operating system variabel in order to when used run different functions for different os
    - the pythonian way of a method that is started after starting the program(long way to say main method) is
    ```python
    if __name__ == *__main__*:
        pass
    ```
    - when the *main method* isnt executed(when a file is imported) or not set in a script, its `__name__` will be set to the name of the file it is in
- `__doc__`
    - contains the docstring
- `__dict__`
    - Python stores values of objects in a *dictionary* with the var name as key `Object.__dict__[Key]`

## Identifiers
- An identifier is a name given to entities like class, functions, variables, etc
- there are special identifiers which are good to know:
    - `_*` => stores the result of the last evaluation
    - `__IDENTIFIER__` => dunder names, system defined identifiers that can alter behavior e.g. `__init__()`
    - `__IDENTIFIER` => represent class private name pattern

## Python Commandline Interface
- link to the python documentation for this: [link](https://docs.python.org/3/using/cmdline.html)
- `python -c` => executes a command given as string after the *-c*
- `python -m` => loads a module and executes it as *__main__*

## Frozen Binaries
- a frozen binary is a packed interpreter along with the modules that are neccessary to execute a program into one binary or package (like in an file.exe for windows)
- tools to create a frozen binary:
    - py2exe
    - PyInstaller
    - freeze
    - cx_freeze

## Python Site-Packages
- the site-packages folder is the place where custom added packages are stored
- its part of the *sys.path*
- own packages has to be stored there in order to be native importable

## Unpacking a Data Structure
- datastructures can be *unpacked* means assigning the content of a datastructure to variables in one go
- e.g.:
```python
    player = (male, elf, hendrik) # a tuple representing a player char is created
    gender, race, name = player # the contend is unpacked into the vars
```
- there has to be the same amount of vars that there are elements within the data structure
