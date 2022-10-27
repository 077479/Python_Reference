# 4 Docstring
## 4.1 Basics
- a docstring or documentation string is a comment at the start of a codeblock (package, module, class, method, function) that explains what the object does
> for functions and methods it is better to document the WHY rather than the How, the how can be seen
- it should appear after the definition of an object
- it is returned through the "help()" function and is the attribute "__doc__" of an object

## 4.2 Comments vs Docstrings
- comments are used to help the devs to understand the intent and functionality of an expression
- docstring is a general documentation that should explain the object

## 4.3 Docstrings for Objects
- **Package**:
    - should be written into the ``__init__.py`` file
    - should mention all aviable modules and sub-packages exported by the package
- **Module**:
    - should list all aviable classes, objects, functions and exceptions that are important for the module
    - should be a one line summary
    e.g.:
    >
        Classes:

            Pickler
            Unpickler

        Functions:

            dump(object, file)
            dumps(object) -> string
            load(file) -> object
            loads(string) -> object

        Misc variables:

        __version__
        format_version
        compatible_formats
- **Class**:
    - should summarize the behavior
    - should list the public methods/instance-vars
    e.g:
    >
        " A class to represent a person.

        ...

        Attributes
        ----------
        name : str
        first name of the person
        surname : str
        family name of the person
        age : int
        age of the person

        Methods
        -------
        info(additional=""):
        Prints the person"s name and age"

- **Funtion/Method**:
    - should summarize the behavior
    - should document arguments/return values
    - should list all exceptions that could be raised
    e.g.:
    >
        Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b

- **Script**:
    - should document the script function and commandline syntax
    - should give a quick reference to all functions and arguments

## 4.4 Different Docstring Formats
- **Epytext**:
    - is used in javascrypt
    >
        This is a javadoc style.

        @param param1: this is a first param
        @param param2: this is a second param
        @return: this is a description of what is returned
        @raise keyError: raises an exception

- **reST**:
    - restructured text
    >
        This is a reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception

- **Google**:
    >
        This is an example of Google style.

        Args:
            param1: This is the first param.
            param2: This is a second param.

        Returns:
            This is a description of what is returned.

        Raises:
            KeyError: Raises an exception.

- **NumPydoc**:
    - is based on google
    >
        My numpydoc description of a kind
        of very exhautive numpydoc format docstring.

        Parameters
        ----------
        first : array_like
            the 1st param name `first`
        second :
            the 2nd param
        third : {"value", "other"}, optional
            the 3rd param, by default "value"

        Returns
        -------
        string
            a value in a string

        Raises
        ------
        KeyError
            when a key error
        OtherError
            when another error

## 4.5 Tool to manage Docstrings
    - link to sphinx: https://www.sphinx-doc.org/en/master/
    - sphinx was created for python doc

## 4.6 Choice
### Package
>
    """
    Package [name]
        [explanation]

    ===== Imports =====

    ===== Modules =====

    ===== Functions =====
    """

### Modul
>
    """
    [package name].[module name]
        [explanation]

    ===== Imports =====

    ===== Globals =====

    ===== Classes =====

    ===== Functions =====

    ===== Exceptions =====
    """

### Class
>
    """
    [package name].[modul name].[class name]
        [explanation]

    ===== Attributes =====

    ===== Methods =====

    ===== Exceptions =====
    """

### Method/Fucntion
>
    """
    [package name].[modul name].[class name].[function/method name]
        [explanation]

    ===== Parameters =====
            
    ===== Returns =====
            
    ===== Exceptions =====

    """