# Basics
- the general workflow of creating a "*distribution-package*" is:
    1. create a source tree (project structure)
    2. prepare a configuration file (containing name, author ...)
    3. create build-artifacts 
        - build aritfacts are the packaged source-tree
        - can be send to distribution like PyPI
        - for python usually a *source distribution(sdist)* or *built distribution(wheel)*
        - created by a built-tool
    4. distibute the build-artifact
> a tool to upload a "*distribution-package*" to PyPI is twine (3rd-party pip installable)


# Source Tree
- just the directory with the files
- usually the root from git or another version control


# Configuration File
## Basics
- the config file tells the "*frontend*" build-tool what backend to use
- needs at minimum
    - `[build-system]` specifying the build-tool
    - `[core metadata]` containing name, version, author. . .
    - `[tool]` configuration for the build-tool
- e.g.
```
[build-system]
requires = [hatchling]
build-backend = "hatchling.build"
```

## Ini
- good for small projects, support 1-level deep hierarchy, easy to read and parse
- parsed with the *built-in* *configparser*
- e.g.
```python
    # config.ini
    [category]
    option = value

    # py file
    import configparser
    config = configparser.Configparser()
    config.read("config.ini)
    config.get("category", "option")
```

## Toml
- are like ini files but allow wider variety of data, and relationships between values
- some of the datatypes are: DateTime, local time, arrays, floats, hexadecimal values
- e.g.
``` python
    # in toml called keys
    title = "My Toml Cofig"

    # in toml called table
    [project]
    name = "Faceback"
    description = "renders the back of the face from a photo of the face"
    version = "1.0.0"
    updated = 1979-05-27T07:32:00Z
    author = "Back Face"

    [database]
    host = "127.0.0.1"
    password = "p@ssw0rd"
    port = 5432
    name = "my_database"
    connection_max = 5000
    enabled = true

    # in toml called Nested `tables` 
    # implies that the elements are different instances of the same object
    [environments]
    [environments.dev]
        ip = "10.0.0.1"
        dc = "eqdc10"
    [environments.staging]
        ip = "10.0.0.2"
        dc = "eqdc10"
    [environments.production]
        ip = "10.0.0.3"
        dc = "eqdc10"

    # in toml called Array of Tables
    # creates a dict with a key for a list of dicts
    # {"testers": [
    #               {"id": 1, "username":"JohnCena", "password": ...},
    #               {"id": 2, "username":"TheRock", "password": ...}]}
    [[testers]]
    id = 1
    username = "JohnCena"
    password = "YouCantSeeMe69"

    [[testers]]
    id = 2
    username = "TheRock"
    password = "CantCook123"

    # py file
    import toml
    config = toml.load("config.toml") # retrives a dict with dicts ...
    config["project"]["author"] # 'Back Face'
```

## yaml
- yaml files utilizing whitespaces to define hierarchy
- extreme easy to read, can represent complex data structures out of the bat
- good parser for python is 3rd-party "confuse"
- e.g.
```yaml
    appName: appName
    logLevel: WARN

    databases:
    cassandra:
        host: example.cassandra.db
        username: user
        password: password
    redshift:
        jdbcURL: jdbc:redshift://<IP>:<PORT>/file?user=username&password=pass
        tempS3Dir: s3://path/to/redshift/temp/dir/
    redis:
        host: hostname
        port: port-number
        auth: authentication
        db: databaseconfig.yaml
```


## Environment Variables
- if it is neccessary to hold data back (for security reasons for example) an env-var might be suitable
- stored in an `.env` file
- BY ALL MEANS NEVER EVER upload these files to git
- can be accessed with the `os.environ.get` 
```env
flask_env=development
flask_app=wsgi.py
compressor_debug=True
```