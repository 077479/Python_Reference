# Basics
- is the std module to create a CLI
- link to the doc: [link](https://docs.python.org/3/library/argparse.html)
- features:
    - use of positional arguments
    - customization of prefix chars
    - support variable numbers of arguments
    - supports subcommands
- e.g.: `ls -l -s -k /var/log`
    - `ls`: the command that is executed
    - `-l`: option to enable long list format
    - `-s`: optoin to print the size of each file
    - `-k`: option to have the size in kb
    - `/var/log`: parameter that provides a path


# Definitions
- **argument**: single part of a CL deliited by a white space
- **option**: type of argument that modifis the behavior
- **parameter**: type of argument that provides additional information



# Workflow
## Flow
1. import the argparse library
2. create the parser
3. add optional and positional arguments
4. execute `parser.parse_args()`

## example
```python
import argparse

parser = argparse.ArgumentParser(description = "brief description")
parser.addargument("Path", metava="path", type=str, help="help text")

args = parser.parse_args()
print(args.Path)
```



# Namespace Object
- `parse_ags()` returns a `namespace object`
- every input argument gets a property in the `namespace object`
- i.e. an argument added to a parser wiht the name: "*Path*" would be accessed by `args = parser.parse_args(); path = args.Path`
- the namespace is basically a dict mapping defined arguments to the given values



# Parser
## Parser Initialization
- `arparse.ArgumentParser()` returns a parser
- `prog=[str]`: changes the in the help shown name of the tool `parser = argparse.ArgumentParser(prog=[tool name])`
- `uasage=[str]`: changes the usage message in the help message `parser = argparse.ArgumentParser(usage="do option something")`
- `description=[str]`: the description shown in the help message (before the actual help message)
- `epilog=[str]`: a message shown after the actual help message `parser = argparse.ArgumentParser(epilog="message here")`
- `prefix_char=[str]`: the char used to determine argument/options `parser = argparse.ArgumentParser(prefix_char="/")`
    - window users are used to use "/" as prefix for arguments
- `allow_abbrev=[bool]` specifies if argparse tries to map incorrect input for argumets to existing arguments
    - an argument called `--name` would be identified even if the user gives `py tool.py --na`
- `add_help=[bool]` toggles the `-h` flag

## Argument Categories
- threre are two basic categories of arguments that can be adde: "***positional***" and "***optional***" arguments
- **positional**: 
    - argparse will demand theese if not given (cant work without it)
    - positional argemnts are defined by there position added (first one fist agument that has to be given in the cli)
    - e.g.: `cp [source] [destiantion]` considered positional arguments
- **optional**:
    - not mandatory arguments
    - if used can alter the behavior of the command
    - syntactically the difference is that optional arguments start with`--` of `-` and positional not

## add_argument
- `parser.add_argument([argument name: str])` adds an argument to a parser
- `action=`: for optional arguments argparse behavior what to do with it can be altered with the `action=[argument]` parameter
    - `action="store"`: stores the value to the namespace (default)
    - `action="store_const", const=42`: stores a constant value each time the argument is provided
    - `action="store_true"`: stores the bool `True` everytime the argument is provided and where not `False`
    - `action="store_false"`: stores the bool `False` everytime the argument is provided and where not `True`
    - `action="append"`: stores a list appending a value each time the option is provided
    - `action="append_const", const=42`: stores a list appending a constant value each time the option is provided
    - `action="count"`: stores an int that corresponds to the times the option is given
    - `action="help"`: shows the help text and exits
    - `action="version"`: shows teh version and exits
    - custom actions can be created
        - the class argparse.Action has to be subclassed and in the init the classname has to be given as parameter to the super call
        - the `__call__` method has to be used to specify the custom behavior
- `nargs=`: by default argparse awaits 1 value after an argument is given
    - `nargs=[int]`: specifies the amount of values argparse will store under the key in the namespace dict
    - `nargs=?`: an optional single value
    - `nargs=*`: flexible number of values, will be stored in a list corresponding to the name as key of the argument
    - `nargs=+`: awaits at leas one value, but multiple can be given
    - `nargs=argparse.REMAINDER`: stores the and all following values as a list corresponding to the name of the argument
- `defaultt=[value]`: specifies a default value if the argument is but no value was given
- `type=[data type]`: by default all values are treated as `str`, but if another type is given argparse will enforce this
    - e.g.: `parser.add_argument("--amount", type=int)` and a char is given, argparse exits with the corresponding error message
    - argparse auto converts the argument into the goal type
- `choices=[iterable object]`: specifies a list of valid values for the argument
    - the value will be checked against the iterable and raise an error if its not valid
- `required=[bool]`: forces a user to provide the value for the argument
- `help=[str]`: the returned help str if -h is used
- `metavar=[str]`: gives an additional name to the var for the help message
- `dest=[str]`: specifies the name of the property in the namespace (default is name of the argument)

### add_mutually_exclusive_group
- group option that cannot coexist like "*silent*" and "*verbose*"
- `parser.add_mutually_exclusive_group()`: returns a group object bound to the parser
- to the group object can be added argument the same way as to the parser
- e.g.
```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-v", "--verbose")
group.add_argument("-s", "--silent")
# if the tool is now called with the "-s" and "-v" option argparse will raise an error
```


# Subparser
- argparse provides the ability to create sub-commands through `parser.add_subparsers()`
- each subcommand can provide a unique set of arguments
- arguments added to the original parser are aviable to all sub-commands