# Basics
- python doc for packaging: [packaging-doc](https://packaging.python.org/en/latest/)
- quickguide for setuptools: [setuptools-guide](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use)
- a "*python package*", also called "*build-artifact*", or "*source-distribution*"
- but at the end its all the same, a container format with the python files in it
- in this document a "*python installable container*" will be called "*distribution-package*"
- depending on vary parameters, in this container can be other files that are needed to run the program
- be not confused, python calls a directory containing `.py` files package, but a with pip installable container is also called package
- to create a python "*distribution-package*" a tool called `build` is used (python built-in module)


# build
- will use a specified build-tool to create the "*distribution-package*"
- there are various build-tools commons are:
    - flit
    - hatch
    - pdm
    - poetry
    - setuptools
    - trampolim
    - whey
- automatically included files through the `python -m build source-destination-folder` are:
    - readme linked in the meta, license linked in the meta
- other files has to be included manually, this process is build-backend dependent
- link to the setup-tool doc: [link](https://setuptools.pypa.io/en/latest/userguide/index.html)


# Build-Tool
- the build-tool does the heavy lifting for the "*distribution-package*" creation
- example source-distribution:
    - **sdist**: `python -m build --sdist source-tree-dir`
- example wheel-distribution:    
    - **wheel**: `python -m build --wheel source-tree-dir`


# Naming
- python suggests the following naming scheme for "*distribution-packages*" 
- the `whl` extension refers to the "*distribution-packages*" container system "*wheel*"
- the python preferred container format
- `{dist}-{version}-{build}optional-{python}-{abi}-{platform}.whl`
- **dist**: the name of the tool/program/framework
- **version**: the version of the tool/program/framework
    - python proposes a specific versioning stated in the **PEP440**
- **build**: the specific build(like nightly), can be ignored
- **python**: the python version (py3 refers to python3 cp refers to CPython)
- **abi**: "application binary interface" defined at processor or os level mostly unintresting for normal python programs
- **platform**: the destination os that in which the tool/program/framework can run
- examples:
    - `chardet-3.0.4-py2.py3-none-any.whl`
    - `cryptography-2.9.2-cp35-abi3-macosx_10_9_x86_64.whl`


# Hierarchy of Distribution Packages
## Packaging Hierarchy
1. PEX - libraries included
2. anaconda - Pyton Ecosystem
3. freezers - python included
4. images - system libraries included
5. containers - sandbox images
6. virtual machines - kernel included
7. hardware - plug and play

## Source Distribution
- distribution created with the `sdist` command that can be installed with **pip**
- used when the package is pure python and the destination system is known to have no version conflicts
- there are 3rd party packages that are depending on "*non-python*" packages, example is "*numpy*"
- therefor it is mostly used when no third party modules need installation

## Wheel
- package format designed to create packages that depends not only on python-source code
- can be installed with **pip** (pip prefers always wheel because its more robust and faster)
> usually if there are dependencies in not interpreted languages like c++ or c
> there are wheels for every destination system where the dependent files are
> specially compiled for the destination system

## Custom Exeutable
- there a ways to generate custom executables for a python project
- this process is called **freezing** because it "*freezes*" the state of the project and provides a container executable that has anything to run the project in it, even the correct python interpreter
- creates a very big distribution 
- tools for that are:
    - single user deployments:
        - pyInstaller => cross platform
        - cs_Freeze => cross platform
        - constructor - for cli installer
        - py2exe => creates only windows executables
        - py2app => creates only mac os executables
        - osnap => windows / mac
        - pynsist => windows only
    - multi component server:
        - Chef Omnibus

## Images / Container
- packaging a full image that runs on its own with own operating systems files on their own
- tools without own kernel:
    - Docker
    - AppImage
    - FlatPak
    - SnapCraft
- tools that inclued an own kernel:
    - Vagrant
    - VHD
    - AMI