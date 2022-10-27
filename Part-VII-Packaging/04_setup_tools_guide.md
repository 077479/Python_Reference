# basics
- setuptools is a python build-tool
- this tool automatically creates the distribution package
- needs a config file called `pyproject.toml` and a config file `setup.cfg`
- link to an article: [link](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)
- assumed package structure:
>
    mypackage
    ├── pyproject.toml ([build-system] table is given)
    |   # setup.cfg or setup.py (depending on the configuration method)
    |   # README.rst or README.md (a nice description of your package)
    |   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
    └── mypackage
        ├── __init__.py
        └── ... (other Python files)
- a call `python -m build` will create a `tar.gz` and a `whl` file


# extra config
## Package Discovery
- the default is that setuptools use the `cwd` as root for the project
- this can altered in one of the config files => pyproject.toml, setup.cfg, <del>setup.py</del>
> 
    # pyproject.toml
    [tool.setuptools.packages.find]
    where = ["src"] # "." by default
    include = ["mypackage*"] # "*" by default
    exclude = ["mypackage.tests*"] # empty by default
    namespaces = false # true by default

    # setup.cfg
    [options.packages.find]  # (always `find` even if `find_namespace:` was used before)
    # This section is optional as well as each of the following options:
    where=src  # . by default
    include=mypackage*  # * by default
    exclude=mypackage.tests*  # empty by default

## Entry Points
- setuptools can create an entry point
> 
    # pyproject.toml
    [project.scripts]
    cli-name = "mypkg.mymodule:some_func"

    # setup.cfg
    [options.entry_points]
    console_scripts =
        cli-name = mypkg.mymodule:some_func

## Dependency Management
- specify additional "*distribution-packages*" that will be installed along with the installation of the program
- each dependency is represented by a line
- accepts equality operators to specify a minimum version
> 
    # pyproject.toml
    [project]
    ...
    dependencies = [
        "docutils",
        "requires <= 0.4",
    ]

    # setup.cfg
    [options]
    install_requires =
        docutils
        requests <= 0.4

## Including Data Files
- specify data that has to be included into the "*distribution-package*"
- the data files must be included in a `MANIFEST.in`
> 
    # pyproject.toml
    [tool.setuptools]
    include-package-data = true

    # setup.cfg
    [options]
    include_package_data = True

## Developer Mode
- a "*pdistribution-package*" that is installed in the "*developer mode*" will not be copied into the system
- pip will just create linkings to the project as if it was installed
- this means changes to the "*distribution-package*" will be reflected by the "installed" program
- `pip install --editable` to install a "*distribution-package*" in "*developer mode*"


# setup.cfg Guide
>
    Metadata
        Key                 Type
        name                str
        version             attr:, file:, str
        url                 str
        download_url        str
        project_urls        dict
        author              str
        author_email        str
        maintainer          str
        maintainer-email    str
        classifiers         file:, list-comma
        license             str
        license_files       list-comma
        description         file:, str
        long-description    file:, str
        keywords            list-comma
        platform            list-comma
        provides            list-comma
        requires            list-comma
        obsoletes           list-comma
    Options
        zip_safe            bool
        setup_requires      list-semi
        install_requires    file:, list-semi
        extras_require      file:, section
        python_requires     str
        entry_points        file:, section
        scripts             list-comma
        eager_resources     list-comma
        dependency_links    list-comma
        tests_require       list-semi
        packages            find:, find_namespace:, list-comma
        package_dir         dict
        package_data        section
        py_modules          list-comma
        data_files          section


# Example
```c
[project]
name = "infer_pyproject"
version = "0.1.0"
description = "Create a pyproject.toml file for an existing project."
authors = [
    {name = "Martin Thoma", email="info@martin-thoma.de"},
    {email = "info@example.com"}
]
license = {file = "LICENSE.txt"}
readme = "README.md"
requires-python = ">=3.6"

keywords = ["packaging", "dependency", "infer", "pyproject.toml"]

classifiers = [
    "Topic :: Software Development"
]

# Requirements: This is done differently by poetry!
dependencies = [
    "Click>=7.0"
]

[project.optional-dependencies]
dev = [
    "black>=18.3-alpha.0",
]

[project.urls]
homepage = "https://github.com/MartinThoma/infer_pyproject"
documentation = "https://github.com/MartinThoma/infer_pyproject"
repository = "https://github.com/MartinThoma/infer_pyproject"

[project.scripts]
poetry = "infer_pyproject.cli:main"

[build-system]
requires = [
    "setuptools >= 35.0.2",
    "setuptools_scm >= 2.0.0, <3"
]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target_version = ['py36']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```