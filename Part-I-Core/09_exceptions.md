# 9 Exceptions
## 9.1 Basics
- an Exception is just an Object that represents an Error that has occured during the program execution
- Errors can be distinct into two categories:
    - Syntax Errors:
        - caused by not following the syntax
        - also called "parsing error"
        - mostly raised when the interpreter analysis a file
    - Logical Error:
        - Error that occurs when the syntax is correct but the statements does not make any sense to the interpreter, or the interpreter does not know how to proceed
- if occured during execution, in both cases the interpreter will call an Exception Class that represents the ocurred error (this process is called "raising an exception")

## 9.2 Raising an Exception
- exceptions can be raised manually in order to make a fellow programmer or ourself aware of a exceptional circumstance
> there is no distinction between another dev and the author when reviewing month old code
- exceptions can be manually raised with the keyword "raise" followed by the exception class to raise
- in python most exceptions has the word "error" at the end of the name
- if in need to pass custom information without the use of a custom exception the "Exception" class should be raised, it will accept a string that will be prompted 
- e.g. ``raise Exception("only odd values should go in here")``
- This is most of the time the preffered way, custom exceptions are mostly used in custom frameworks, libraries or APIs where the author wants to make the user or another dev aware of a specific information about an error
> in python the word Error and Exception is often used interchangeably

## 9.3 List of common Built-In Exceptions
- **AssertionError**:  assert statement fails
- **AttributeError**: attribute/reference assigment fails
- **EOFError**: input hits the end-of-file condition
- **FloatingPointError**: floating point operation fails
- **GeneratorExit**: generators close method is called
- **ImportError**: imported module is not found
- **IndexError**: called index is out of range
- **KeyError**: key is not found
- **KeyboardInterrupt**: keyboard interrupt
- **MemoryError**: out of memory
- **NameError**: variable is not found within the namespaces
- **NotImplementedError**: abstract methods
- **OSError**: system operation cause an system error
- **OverflowError**: operation is too large to be represented
- **ReferenceError**: weak reference proxy for accessing garbage collected reference
- **RuntimeError**: error does not fall under a predefined error category
- **StopIterationError**: raised by the next function
- **SyntaxError**: syntax error raised by the parser
- **IndentationError**: incorrect indentation
- **TabError**: indentaion consists of tabs and whitespaces
- **SystemError**:interpreter detects internal error
- **TypeError**: function does not apply to the object
- **UnboundLocalError**: reference is made to a var without value
- **UnicodeError**: unicode en/decoding went wrong
- **ValueError**: function gets correct type but false value
- **ZeroDivisionError**: division by zero

## 9.4 Effect of an Exception
- the execution of the program will be stopped
- if not handled the exception will lead to the exit of the program

## 9.5 Handling an Exception
- Exception handling can be used to control the program flow like an "else ... if" statement
-to handle an exception the suspiciouns code has to be wrapped by a "try ... except" block
- e.g.:
```python
try:
    # suspicious code
except <ExceptionClass>:
    # handling an ocuured exception
```
> note that the except statement works without further arguments(the exception class) BUT this has to be avoided, other devs will be mark that as syntax failure! see hierarchy of exceptions
- it is possible to give the except statement more than one Exception Class as argument in order to catch more than one occuring exception class
- also it is possible to stack exception statements in order to deal with different exceptions differently
- e.g. (when stacked only the first exception that is caught will be handled if more were raised they are gone)
```python
try:
    # pretty suspicious code
except (ValueError, IndexError):
    # handle value error here
except KeyError:
    # handle key error here
```
- to access the Exception Object it can be passed after the except statement withe "as"
- e.g. ''except ValueError as e '' (mostly interesting for custom exceptions)
- the name of the passed exception object can be choosen freely, but "e" or "ex" has become established
- to further control the program flow there are two more keywords usable with exceptions "else" and "finally"
- the else codeblock will be executed if there has no exception occured
- the finally codeblock will be executed regardless of the occurance of an exception (often used to close an db connection of a file or something like that)

## 9.6 Exception Hierarchy
- the python exception hierarchy looks like:
    >
        BaseException <= SystemExit
                         KeyboardInterrupt
                         Exception          <= most if not all of the other exception
- we can see that almost all exception are subclasses of "Exception"
- if custom exception are created most of the time they should derive from "Exception" too
- which is also a subclass of "BaseException"
- an "except" statement with no parameter passed will catch all Exception that are deived from BaseException, therefor the "SystemExit" and the "KeyboardInterrupt" exception, which should only be caught when really neccesarry
- if in need to catch all built-in exceptions use "except Exception", if really in need to catch ALL exceptions use "except BaseException" (this will show fellow programmers our intend, a "except" statement without a parameter will be seen as syntax failure)

## 9.7 Defining Custom Exceptions
- when none of the built-in exceptions are fitting a custom exception can be created, it should derive from "Exception" and can be handled like any other class
- the name of the custom exception should show the reason why it is raised => ``UserNotFoundError``
- custom Exceptions are mostly used when creating an "framework", "API", or a "library" that is intended to be used by otehr devs