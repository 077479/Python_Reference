# Basics
- the configfile is accessed by build to specify the build process
- the configfile should have to be named `pyproject.toml`
- addidional information can be given in a `setup.cfg` file or a <del>setup.py</del> file
> configuring a project with a setup.py is deprecated


# build-system
- ***[build-system]***: the "build system" category is required and defines how the package should be build
- ***requires***: list of packages that are needed to build the package (pip will install them as dependencies when this is installed)
- ***build-backend***: the object that will perform the build
- e.g.
>   
    # setuptools
    [build-system]
    requires = [setuptools>=61.0]
    build-backend = "setuptools.build_meta"

    # hatchling
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"


# Metadata
- link to the doc: [metadata-doc](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata)
- ***[project]***: under the project category the meta data is stored
- ***name***: name of the package
- ***verion***: the veriosn of the distribution, look at this for versioning
    - [pep440](https://peps.python.org/pep-0440/)
- ***author***: every author should be named with email adress
- ***maintainer***: every maintainer should be named with email adress
- ***description***: one sentence summary of the functionality
- ***readme***: path to the readme file (shown on the package detail in PyPI)
- ***license***: path to LICENSE
    - [license-choolser](https://choosealicense.com/)
- ***requires-python***: specifies the python version needed
- ***classifiers***: short summary of the meta data
- ***[project-url]***: links shown on PyPI
- e.g.
>
    [project]
    name = "example_package_YOUR_USERNAME_HERE"
    version = "0.0.1"
    authors = [{ name="Example Author", email="author@example.com" },]
    description = "A small example package"
    readme = "README.md"
    license = { file="LICENSE" }
    requires-python = ">=3.7"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",]

    [project.urls]
    "Homepage" = "https://github.com/pypa/sampleproject"
    "Bug Tracker" = "https://github.com/pypa/sampleproject/issues"