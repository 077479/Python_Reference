# 3 Functions/Return/Lambda
## 3.1 Functions
- a function is a group of related statements, that perform a specific task 
> a one time written codeblock that can be executed everytime it is called
- with functions a program can be decomposed into smalll segments (for reusability, maintainability)
- functions are declared with the keyword ``def``
- ``def function_name():``
- everything that is nested after a the function declaration is considered the functions codeblock
- the function ends when the end of the nesting
- e.g.
```python
def function_name():
    pass # in the function
    pass # in the function

pass # not in the function

function_name() # will call the function and execute the code within the function
```
- a "function call" is made by simply writing the name of the function with brackets

## 3.2 Positional Arguments
- functions can be given arguments
- arguments are variables that are accessable within the namespace of the function
- arguments are created by stating them in the bracket within the ***"def"*** statement after the name
- e.g. ``def function_name(argument_1, argument_2):``
- in the function call the arguments have to be provided ``function_name(True, False)``
> within the functions namespace the variables argument_1 and argument_2 are aviable through the name stated in the definition of the function and will have, the in the function call given, value
- if just the value is provided by the calling code the positional arguments are tied to their position (i.e. the first provided value will be the value of the first declared argument and so on)
- but the value can be given like a keyword with the ``=`` operator ``function_name(argument_1=True, argument_2"=False)``
- when the keyword version is used by the calling code, the order of the given values does not matter

## 3.3 Default Arguments
- default arguments are arguments that have a predefined "default" value
- theese arguments must not be provided on a function call
- if not provided they will be set with their default value given in the function declaration
- e.g. ``def function_name(arg, arg_default=False):``
    - "arg" is a positional argument that has to be provided on a function call or the call will raise an exception
    - "arg_default" is a default argument it can be provided but it isnt mandatory, if not provided python uses the given default value
- the positional arguments still have to be provided, but the default arguments can be provided
- default arguments can be used like positional arguments
- example 1 ``function_name("positional arg_1", "default arg_1")`` the value is just given
- example 2 ``function_name("positional arg_1", arg_default="default arg_1")`` the value is given with keyword notation
- if the keyword version is used, the order of the "default arguments" dont matter, BUT the order of the not keyword notation used arguments matter!
> default arguments are set when the interpreter goes through the code, if tied to a global var and the global var changes during execution the default value wont change

## 3.4 Variable Argument Lists
- python provides a variable argument assignment, when the amount of arguments passed to a function isnt clear, the arguments can be stored into a tuple where all passed arguments will be stored (the tuple will be fifo => first in first out)
- this functionality is done by using the ``*`` operator
- e.g. ``def get_webpages(*links):`` the given links will be stored in a tuple and can be processed within the function, if no argument is provided the tuple will be empty
- by convention the tuple should be named ***"args"*** but can freely be named

## 3.5 Arbitrary Arguments
- there is also a way to store "keyword arguments", passed to a function, in a dictionary (will make sense after data structures is read)
- it works like the variable argument list but with keywords
- this functionality is done by using ``**`` before the name of the dictionary
- e.g. ``def keyword_function(**key_word_args):``
- often used to set options:
```python
class Options:
    default_options = 
    {
        "port":21,
        "host":"localhost",
        "username":None,
        "password":None,
        "debug":False
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]
```
- the convention is to name the arbitrary argument dictionary ***"kwargs"*** or ***"kw"*** but the name can freely be choosen

## 3.6 Arguments Example
```python
def augmented_move(target_folder, *filenames, verbose=False, **specific):
# function to copy or move files on disk

    def print_verbose(message, filename):
        # if extensive output is needed as response
        if verbose:
            print(message.format(filename))

    # actual logic
    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        
        if filename in specific[filename] == "ignore":
            print_verbose(f"ignorinng {filename}")
        
        elif specific[filename] == "copy":
            print_verbose(f"copying {filename}")
            shutil.copyfile(filename, target_path)

        else:
            print_verbose("moving {filename}")
            shutil.move(filename. target_path)

# function calls
augmented_move("location", "file1", verbose=True)
augmented_move("location", "file1", "file2", "file3", "file2"="ignore")
```

## 3.7 Unpacking Arguments
- containers such as lists or dicts can be unpacked automatically when used as arguments
- use the "*" operator to unpack lists, sets and tuples
- use the "**" operator to unpack dictionaries, BUT the keys must be the names of the arguments of the function (dictionaries will be unpacked from left to right)
```python
x = {"a":1, "b":2}
y = {"b":7, "c":3}
z = {**x, **y} # {"a":1, "b":7, "c":3}
```
- BUT the normal rules for function arguments apply, positional args must be given, and the amount of args must be right for the function

## 3.8 Functions are Objects
- in python functions are objects
- attributes can be set to functions through the "dot" notation
- functions can be passed around like objects (also applies to methods)

## 3.9 Return
- every function will return a value
- this value can be spcified with the "return" keyword
- if the "return" value is not specified the function will return "None"
- be aware the return statement ends the function emmidiatly!

## 3.10 Recursion
- a recursive function is a function that calls itself
- within the developer community recursive functions/methods are seen as elegant
> devs are tending to use them as a sign of superiority and craftmanship. But they are difficult to read/maintain. There are usecases for recursions and there are not, bare that in mind
- an example of a real world situation could be two mirrors infront of each other, every item between them is seen recusively
- every recursive function/method must have a base condition, that ends the function, to avoid an infinite loop
- by default the python interpreter limits the recursion depth to 1000 after that a "RecursionError" will be raised (can be changed)
- e.g.
```python
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
```
- Adventages:
    - makes code look clean
    - complex tasks can be broken down
    - sequence generation/processing is easier
- Disadventages:
    - the logic of a recursion is hard to follow
    - its expensive in processing time and memory usage
    - its hard to debug
> remember freeman dyson with "a good scientist is a person with original ideas. A good engineer is a person who makes a design that works with as few original ideas as possible. There are no Prima Donnas in engineering"

## 3.11 Lambda
- lambdas or anonymous functions or functions without a name
- lambda functions are generated by the keyword "lambda"
- e.g. ``lambda argument: expression`` (the expression is executed)
- can have unlimited amount of "arguments" but only one "expression"
- expression is evaluated and returned
- can be used everytime a "function object" is required
- used as "throwaway" functions (when a function is only needed a short period of time)
- typically used with "filter()", "map()", "reduce()"
- when a lambda function isnt assigned to a var (when the return value ist stored) it is called anonymous function
- e.g.:
    - ``lambda x: x*x`` - will return the given argument multiplied by itself (risen to the power of 2)
    - ``import subprocess; clear = lambda: subprocess.run("clear", shell = True)`` # assigns the given command to the variable clear