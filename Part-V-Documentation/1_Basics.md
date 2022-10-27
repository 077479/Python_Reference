# Basics
- "code is more often read than written"(Guido van Rossum, PyCon)
- "code tells you how, comments tell you why"(Jeff Atwood)
- code is written for two audiences, "*the user*" and "*other developers*"

# Definitions
- **commenting**: describes the code for developers, helps guide the reader to an understanding of the code, its purpose and the design
- **documenting**: describes the functionality to users, to help them unleash the full potential of the written tool
- **docstring**: a docstring is a multiline comment that is hard-coded into the implementation in order to describe them

# Comments 
- in python created with `#` (line comment)
- should be a brief statement
- PEP8 defines that comments never should exceed 72 chars
- even if the code has the suggested limit of 80 chars the comment then has to be spanned over multiple lines

## Puropose
- **Planning, Reviewing**:
    - often comments are used to outline sections of code
    - to look how the different components might look like
- **Code Description**:
    - explains the intent of the code
- **Algorithmic Description**:
    - it is usefull to explain complicated mechanics that are used
    - if there are dependenciies this should mention the dependencies
- **Tagging**:
    - lableling specific portions of the code
    - like `# Storage` or `# CLI Interface`

## General Rule
- general rules suggested by Jeff Altwood
1. Keep comments as near to the described code as possible
2. dont use complex formatting
3. dont include redundant information
4. create clear readable code (clear readablle code does not need explanations)

# Type Hinting
- python added in 3.5 the possibility to create "*comments*" within the code itself
- this is called type hinting
- parameters get the type that they expect direct into the code
- methods or functions get the return type direct into the code
- this enables the reader to immeidiatly see what the function awaits and what it returns
- leads to a better understanding of the code
- the syntax is `parameter: [type]` and `def function_name() -> [return type]`
- **e.g.**
```python
def hello_there(name: str = "Kenobi") -> str:
    return f"hello there general {name}"
```

# Docstrings
- the python documentaion is centered on docstrings
- docstrings are created by enclosing the comment with `"""` or `'''`
- python takes the first "*multiline*" comment of the object and uses is as docstring for it
- these comments are native spanned over multiple lines (means without the use of `\`)
- docstrings will be returned with the python built-in function `help()`
- inernally python stores this on the variable `__doc__` in the specific object
- the docstring convention is described in the PEP 257

## Purpose

## General Structure
- **one line summary**
- **blank line proceeding the summary**
- **further information**
- **blank line**

## General Rules
- max lengt 72 chars

## Docstring Categories
## functions/methods
- created in the function/method
- placed immediatly after the declaration
- at the same level as the codeblock
- **contains**:
    - brief description what the function/method does
    - any arguments
    - optional arguments(or these with default values) has to be labled as these
    - any side effects when executing the function/method
    - any exception that can be raised
    - any restricion on when the method can be called (prequesitions like "*db access has to be established*")
- **e.g.**
```python
def says(self, sound=None):
    """Prints what the animals name is and what sound it makes.

    If the argument `sound` isn't passed in, the default Animal
    sound is used.

    Parameters
    ----------
    sound : str, optional
        The sound the animal makes (default is None)

    Raises
    ------
    NotImplementedError
        If no sound is set for the animal or passed in as a
        parameter.
    """
```

## Class Docstring
- created for the class
- placed immediatly after the class declaration
- at the same level of indention as the codeblock
- **contains**:
    - summary of the purpose of the class and behavior
    - public methods, along with a brief description
    - class properties
    - if the class is intended to be subclassed anything related to the interface for the subclasses
    - the description of the `__init__` is aswell in the method itself
    - unlike in functions the summary of the `__init__` method can be omitted
- **e.g.**
```python
    class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
```

## Module
- created to get an overview of the modul
- placed on the top of the file
- **contains**:
    - summary of the purpose of modul and behavior
    - public function, along with a brief description
    - classes, along with a brief description
    - exception that ccan be raised

## Package
- placed on the top of the package in the `__init__.py`
- list of the modules and sub-packages with a brief description

## Script
- scripts are cosidered single executive run from the console
- the docstring is placed on the top of the file
- should be returned with the -h option
- should be a description of the usage of the script, with all commands, options and parameters
- any third party dependencies has to be mentioned
- **e.g.**
```python
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd

def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()
```

## Project
### Private Projects
- readme: a README file with a brief summary of the projects purpose, including requirements for installation or operation
- `example.py` a file that gives simple examples of the functionality
### Shared Projects
- Readme: A brief summary of the project and its purpose. Include any special requirements for installing or operating the project. Additionally, add any major changes since the previous version.
- `example.py` a file that gives simple examples of how to use the project
- "*how to contribute*" include how new contributers to the project can contribute
### Public/Open Source Projects
- Readme: A brief summary of the project and its purpose. Include any special requirements for installing or operating the projects. Additionally, add any major changes since the previous version. Finally, add links to further documentation, bug reporting, and any other important information for the project. Dan Bader has put together a great tutorial on what all should be included in your readme.
- How to Contribute: This should include how new contributors to the project can help. This includes developing new features, fixing known issues, adding documentation, adding new tests, or reporting issues.
- Code of Conduct: Defines how other contributors should treat each other when developing or using your software. This also states what will happen if this code is broken. If you’re using Github, a Code of Conduct template can be generated with recommended wording. For Open Source projects especially, consider adding this.
- License: A plaintext file that describes the license your project is using. For Open Source projects especially, consider adding this.
- docs: A folder that contains further documentation. The next section describes more fully what should be included and how to organize the contents of this folder.

# Docstring Formats
- the used deocstring is "*NumPy/SciPy-style*" docstrings

## Google Docrtring Example
```python
"""Gets and prints the spreadsheet's header columns

Args:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""
```

## ReStructured Text Example
```python
"""Gets and prints the spreadsheet's header columns

:param file_loc: The file location of the spreadsheet
:type file_loc: str
:param print_cols: A flag used to print the columns to the console
    (default is False)
:type print_cols: bool
:returns: a list of strings representing the header columns
:rtype: list
"""
```

## NumPy/SciPy Example
```python
"""Gets and prints the spreadsheet's header columns

Parameters
----------
file_loc : str
    The file location of the spreadsheet
print_cols : bool, optional
    A flag used to print the columns to the console (default is False)

Returns
-------
list
    a list of strings representing the header columns
"""
```

## Epytext Example
```python
"""Gets and prints the spreadsheet's header columns

@type file_loc: str
@param file_loc: The file location of the spreadsheet
@type print_cols: bool
@param print_cols: A flag used to print the columns to the console
    (default is False)
@rtype: list
@returns: a list of strings representing the header columns
"""
```

## Personal Favorite
```python
# Package
"""
Package _

===== Imports =====

===== Modules =====

===== Functions =====

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# Modul
"""
module _

===== Imports =====

===== Globals =====

===== Classes =====

===== Functions =====

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5

===== Exceptions =====
"""

# Class

"""
class

===== Attributes =====

===== Methods =====

===== Exceptions =====
"""

# Method/Fucntion
"""[modul/class: _] function/method _:

===== Parameters =====
        
===== Returns =====
        
===== Exceptions =====

"""
```

# Doc Folder Structure
<table>
<tr> <th>Directory</th> <th>Content</th> </tr>
<tr> <td>doc/user</td> <td>documentation for the user, every functionality explained to a user goes here</td> </tr>
<tr> <td>doc/administration</td> <td>documentation for functionality that requires for the user elevated access</td> </tr>
<tr> <td>doc/api</td> <td>documentation for the API</td> </tr>
<tr> <td>doc/development</td> <td>information for contributers or related process/style guides</td> </tr>
<tr> <td>doc/legal</td> <td>legal documents like License</td> </tr>
<tr> <td>doc/install</td> <td>instructions for installation</td> </tr>
<tr> <td>doc/update</td> <td>update instructions/ changelog</td> </tr>
<tr> <td>doc/topic</td> <td>indexes per topic plus lik to all the ressources under that topic</td> </tr>
</table>

# Documentation Guiadence
- Categories for software documentaion
    - tutorial[learning oriented]: turn learners into users
    - how to guides[problem oriented]: guides to take the reader through steps to solve a problem
    - reference[information oriented]: description of the machine
    - discussions[understanding oriented]: explanations to create understanding of a topic (gives context to get connections, design decisions, examples, alternative approaches...)
- the documentation should aim to theses categories
- these categories should be separated (as much as possible)
> 
                [practical]
                    │
    Tutorial        │ How-To-Guides
    (Learning)      │ (Problem)
                    │
    ─────[studying]─┼─[coding]─────────────
                    │
    Discussions     │ Reference
    (understanding) │ (information)
                    │
                [theoretical]



# Documentation Tools