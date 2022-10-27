# 8 File Operations
## 8.0 Preface
- The Problem with Python Filehandling is that previous file paths were represented by text strings to the location supported by the "os.path" standard lib
- this works but, since paths arent strings there were functionality missing, this missing functionality was then spreaded in modules around the standard library like "glob", "os", "shutil"
- the next thing is, strings can be easily manipulated which sounds good for file paths but is usually not such a great idea
- e.g. to join two paths to access a file the concatenation (+) can be used to add a string, but then there has to be some statement to distinct different "path separator symbols", therefor the "os.path.join()" function is used it chooses the correct separator automatically
- in python 3.4 the pythlib module was introduced to deal with these challenges, it gathers the functionality in one place through a "path object" that represents a file path

## 8.1 File/Directory operations
- **Basics**:
    - files are named locations on a disk
    - the order of file operation is:
        1. Open a File
        2. Read and/or Write
        3. Close the File
    - python uses a File Object to manipulate data stored on disks
    - a File object is returned with the ``open("FILE", argument, encoding)`` statement
    - the argument given to the constructor of the file object determines its purpose
        - ``r`` opens the file for reading only (the default)
        - ``w`` opens a file for writing
        - ``x`` will create a new file, raises an exception if the file already exists
        - ``a`` opens a file for appending at the end of it, creates a new file if there is none
        - ``t`` opens a file in text mode (default for reading/changing text)
        - ``b`` opens a file in binary mode to work with non text files
        - ``+`` opens a file for updating
    - the default encoding is platform dependent (windows: cp1252 linux utf-8)
    - when writing to files the "new line feed" has to be added manually!
- **Methods**:
    - ``file.close()`` closes the file object
    - ``file.flush()`` flushes the write buffer of the file stream // the transfer of a computer data from temporary storage(or a stack) to the permanent storage (or into the)
    - ``file.read(n)`` reads n chars from the file
    - ``file.readable()`` returns "true" if the stream can be read from
    - ``file.readline()`` reads and returns one line from the file
    - ``file.readlines(n)`` reads and returns n lines from the file
    - ``file.seek(n)`` changes the "pointer" in the file object to postion n
    - ``file.tell()`` returns the current pointer location
    - ``file.writable()`` returns true if the file stream can be written to
    - ``file.write("string")`` writes a given string into the file, returns the amount of chars written
    - ``file.writelines()`` writes a list of lines to a file
- **best practice**:
    - good practice is to use a finally block to garantee closing the ressource
- **with**:
    - when in need of file operations the built-in function "with" should be used, it will close the file object automatically 
    > ``with`` starts a context manager system implemented in python see **part II 15 Context Manager**
    - with the with statement the "__enter__", "__exit__" methods of the file object will be called at the beginning and end of the nested code
    - it ensures that the ressource is closed no matter what
    - e.g.
    ```python
    with open("path_to_file") as file:
        for line in file:
            pass
    ```

## 8.2 Directory operations
- the "os" module provides many useful methods to work on directrories
- ``os.getcwd()`` returns the current directory, uses double backslashes as divider for directories
- ``os.chdir("PATH")`` change to a directory
- ``os.listdir()`` takes a path and returns a list with the content of the path, defalut is the **C**urrent **W**orking **D**irectory (cwd)
- ``os.mkdir("DIR")`` creates a new directory
- ``os.rename(source, destination)`` does what it says
- ``os.remove("FILE")`` removes a file
- ``os.rmdir("DIRECTORY")`` removes a directory when it is empty
- ``os.shutil.rmtree("DIRECTORY")`` removes a not empty directory

## 8.3 Pathlib
- the thing is the way to process files is not user friendly, the functionality is scattered through three different modules and the way pths to files are handled isnt really good or modern
- to cope with that the ``pathlib`` library was implemented
- the ``pathlib`` module treats file locations as objects and combines the needed functionality in one place
- link to the pathlib doc: https://docs.python.org/3/library/pathlib.html
- link to a cheat sheet: https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf
- the functionality is divided into top level functions and a Path object
- Path objects provide functionality to make basic file operations like deleting replacing
- **Path**:
    - ``pathlib.Path.cwd()``: returns a path object that represents the current working dir
    - ``pathlib.Path.home()``: returns a path object that represents the users home dir
    - ``pathlib.Path([DESTINATION])``: returns a pathobject that represents the destination (dir or file)
    - ``pathlib.Path()`` accepts extra given argumets that are statet after the function call and that start with ``/``
    - e.g. ``pathlib.Path.cwd() / "data" / "scripts" / "test.py"`` returns a Pathobject that leads to "current destination\data\scripts\test.py"
    - the "joinpath()" method adds several locations together e.g. ``pathlib.Path.cwd().joinpath("data", "scripts", "test.py")``
    - ``open()`` function that calls the ".open()" function direct to a path object 
    > the file opbject closes automatically
    - e.g.
        ```python
        for line in Path.open():
                print(line)
        ```
    - ``read_text()`` opens the path in text mode and returns the contents as string
    - ``read_bytes()`` opens the path in text mode and returns the contents as byte string
    - ``write_text()`` opens the path and writes the data to it as text
    - ``write_bytes()`` opens the path and writes the data to it as byte string
    - ``exists()`` returns a boolean value that represents the existance of the destination of the path object
    - ``is_dir()`` returns a boolean value that represents if the pathobject refers to a dir
    - ``is_file()`` returns a boolean value that represents if the pathobject refers to a file
    - ``glob([PATTERN])`` returns a list with pathobject that represents the files in the dir that matches the pattern 
    > pattern could be "*.md" or "file.*"
    - ``rglob([PATTERN])`` returns a list with pathobject that represents the files in the dir that matches the pattern recurses through all subdirectories
    Object Properties:
    - ``name`` returns only the filename as str
    - ``parent`` returns the directory (as path object) of the file or if it represents a dir returns the parent dir
    - ``parents`` returns an iterator object with all parents til root
    - ``stem`` retunrs teh filename without the extension
    - ``suffix`` returns the extension as str
    - ``suffixes`` returns all extensions in case of "file.tar.gz" or similar
    - ``anchor`` returns the root (or the drive on windows) as str
    - ``parts`` returns a list where the elements are the parts between the file separator of the path(includes the file)
- **Top Level Functions**:
    - ``rename()`` renames the represented object
    - ``replace()`` replaces the represented object
    - ``rmdir()`` removes directoy
    - ``touch()`` creates the file if it doesnt exist