# 10 Virtual Environments
## 10.1 Basics:
- link to the doc: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html
- python stores all installed modules in a specific place
- if a module has different versions, they are all stored in the same directory
- if different modules need different versions of a third party module it comes to unexpected behavior or errors
- therefor python provides the possibility to create an own "python virtual environment" to create complete separated environments
- included in python 3 as "venv"
- in python 2.x "virtualvenv" has to be installed
- there are 3rd partie virtual environment tools but if not a specific functionality isneeded just choose one and stick to it
> just bare in mind that is it a good practice when in need of 3rd party packages/modules to use a virtual env

## 10.2 venv:
- venv is the built-in module to create virtual environments (in lower than 3.6 its called pyenv)
- ''python -m venv "NAME"''
    1. "python" is the exe of the interpreter
    2. "-m" when passed uses a module
    3. "venv" the name of the module to use with the "-m" parameter
    4. "NAME" the name of the new virtual environment
- will create a directory with the given name of the virtual env
- directory structure:
>
    env/
        bin/scripts: # files that interact with the virtual environment
        include c: # headers that compile python packages
        lib: # copy of the python version along with all installed packages from the host
- in the "bin/scripts" folder is a activation file, which will activate the virtual environment (seen on the change of the curser)
- when activated all python related commands are executed by the interpreter of the virtual environment even pip installs are only affect the virtual env
