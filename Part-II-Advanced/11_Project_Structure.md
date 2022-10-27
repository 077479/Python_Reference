# 11 Project Structure
## 11.1 Basics
- the idea is to use a standardized project structure that you can work with
- there are several different templates that suggest theese or sose project structure
- in the end a structure should be choosen that works for the dev
> besides most companies have a compliance rule how to structure projects in their wiki
- a structure that works for me is
>
    [] project root/
    │
    ├── docs/
    │
    ├── [package_name]
    │    ├── __init__.py
    │    ├── package_name.py
    │    ├── pytest.ini
    │    ├── data/
    │    ├── tests/
    |    |    ├── src
    |    |    ├── sub_package_I
    |    |    └── sub_package_n
    │    ├── src/
    │    ├── sub_package_I
    │    └── sub_package_n
    │
    ├── wheel/
    ├── LICENSE.txt
    ├── pyproject.toml
    ├── README.md
    ├── .gitignore
    └── setup.cfg

- **project root**
    - the root of the project where all project related files will land
    - **docs**
        - folder for project related documents:
        - drafts, project analisys, images
        - changelog comes here
        - roadmap comes here
        - software requirements document comes here
        - compliance rules comes here
    - **wheel**
        - the installabel or executable versions of the project
    - **License**
        - the license under which theproject is published
    - **pyproject.toml** / **setup.cfg**
        - the config and setup files for the build-tool
    - **README.md**
        - the readme file
    - **package name**
        - the actual package folder
        - i like to name it like the project itself
        - **package_name.py**
            - the entry point of the package
        - **pytest.ini**
            - the config file for pytest
            - i tend to use pytest as testing framework
            - but i also like the unittest way of structuring tests
        - **data**
            - data for the package like configs or hardwired data
        - **tests**
            - the test suite
            - i like to incluede the test suite in the package for other devs 
        - **src** / **subpackage_I ... subpackage_n**
            - i tend to modularize projects
            - and the actual functionality goes here
            - whereas every other added functionality gets its own folder and is handled as separate package of its own
            - an example of this were a ``command line interface``, it would get his own sub_package
            - this helps me to use it again if needed in another project
            - a neat side effect is that i have clear responsibilities for every functionality