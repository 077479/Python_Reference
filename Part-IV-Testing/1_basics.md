# Bascis
- Tests ensure that a program works like intended
- There are several different forms of tests
- usually tests are categorized into **unit** tests, **integration** tests, **End to End** tests
- befor they are getting used to proper test suits, most of the devs have done exploratory tests
    - exploratory tests are tests that are done manually where a dev "*explore"* the API of the progam and makes sure thet a specific input leads to a specific output
    - often a list of all features of a progran is created during the implementation of the features
    - then everytime a change is made the complete list has to be run manually
- this solution is time consuming and the written tests arent easy maintainable
- automated testss are the better way
    - automated testing is the execution of a testplan 
    - a definition of the features to be tested, the order in which they are tested, and the expected results
    - the testplan is executed by a script
- a test is conducted via a"*assertion*", this means checking a value/state against a predefined value/state
- python provides the `assert` command
- a test of a *sum function* would look like: `assert sum([1,2,3]) == 6`
- as a rule of thumb when writing tests:
    - make sure tests are repeatable and run the tests a couple of times to make sure hte result is consistent
    - assert results that relate to the input data
- it is good practice to first write a test that always fail and a test that always pass, just to make sure the testframework runs as expected

# Explanations
- ***test suit***: the complete test structure of a program is called "*test suit*"
- ***test plan***: a checklist of test cases (which test for which feature at which point)
- ***test runner***: a test runner is the script that processes the scripts
    - lives through 2 phases:
    1. *discovery*: detect and gather all tests
    2. *run*: run the tests one after another

# Test-Case
## Basics
- a test case is a set of actions on a system, to determine if it satisffies the requirements
- a test case is composed of:
    - **Perconditions**: defines teh state of the unit to be able to execute teh test-case
    - **Steps**: actions that have to be done during the test-case with the expected behavior
    - **Postconditions**: defines the state in which the unit has to be after the actions are done

## Creating a Test Case
- answer following two questions:
    1. what do you want to test?
    2. which kind of test do i need for that? (unit test, integration test, ...)

## Example
- Test Case 2.2 - Change User Password
>
    Precondition
        1. The user ***User1*** exists
        2. The user is logged in as ***User1***
        3. The user is at the ***main menu***

    Actions
        Nr  Action                                  Expected-Response                                       Success/Fail
        ----------------------------------------------------------------------------------------------------------------
        1   Click the change passphrase button      The system shows a dialog to insert a new passphrase
        2   Enter new passphrase                    The dialog shows an asteriks for each typed char
        3   Click the send button                   The system shows a dialog with a success message
        4   Wait 2 seconds                          The dialog goes away

    Postcondition
        - the passphrase of User1 passphrase changed to new passphrase

# Organizing Tests
- its common to organize tests within an own folder either in the `root` dir or in the `src` dir according to the structure
- it is also common to separate the `unit tests` from the `integration tests`
- data needed to run through tests that will be provided as predefined "*sample*" data is called ***fixture***
- fixtures should be in a separate folder too (usually where they are needed in the integration test folder)
>
    root/
    └── tests/
    |   ├── test_integration/
    |   |   └── test_integration1
    |   |   
    |   ├── test_Unit/
    |   |   ├── test_unit1
    |   |   ├── test_unit2
    |   |   |
    |   |   └ fixtures/
    |   |      ├── test_basic.json
    |   |      └── test_complex.json
    |   |
    |   └── test_EndtoEnd/
    |       └── test_e2e

#  Test Pattern:
- the tests should follow the following pattern:
    1. Arrange
        - set the tested system into the precondition state
    2. Act
        - run through the actions
    3. Assert
        - check the state of the system with a prior defined state (is the system in the expected state)
> static tests are code linters, where the code doesnt have to run, and mostly the IDE does this in realtime through the implementation
- **example**
```python
import unittest

class test_one(unittest.TestCase):
    def test_something(self):
        # Arrange phase
        test_data = ["all", "tests", "are", "hmmh"]

        # Act phase
        ret_value = capitalize_function(test_data)

        # Assert phase
        assert ret_value == ["ALL", "TESTS", "ARE", "HMMH"]
```

# Testing Models
##  Basics
- to balance the cost of testing with the cost of developing in order to get the most out of development processes different testing models were created
- the two main testing models are the "*Testing Pyramid*" and the "*Testing Trophy"*

##  Testing Pyramid
- originates from the book *"Succeeding with Agile"*
- the main statements are:
    - write different tests (unit, functional, E2E, ...)
    - the higher the level gets the lesser should be tested (i.e. the more abstract the tests are the less tests should be there)
    - means tons of unit tests, good amount of integration tests, but only a few system or E2E tests
- the idea is with a good amount of "*cheap*" unittests the system should be robust enough to just test the minimum amount of "*cost intensive*" tests

##  Test Trophy
- originates from the author of many often used JavaScript technologies
- the main statement is:
    - write not too many tests
    - but focus on integration tests (to make sure components work together)
    - means okish amount of unit tests, tons of integration tests, a few E2E tests

# Distribution and Coverage
- it gives almost no interest return in testing getters and setters!
- so it isnt intendet to test every bit of code
- the sweet spot between test-coverage and return of interest is seen around 80% coverage
- the rule of thumb is the more complex a function is the more it should be tested
> also means the more compact a language is the more complex statements can be made the more the statements should be tested
- the testing should not end with the release
    - often sysems tests are neglected so that issues that happen in productive environments are only found by the users/clients

# automated test runs
## Basics
- it is common to automate the test runs, i.e. automated run of specified tests linked to a condition like `git add` command
- tools for that are called CI/CD Tools (Continious Integration/ Continious Deployment)
- these tools run the tests, compile and publish any application, and even deploy them into production
- an often used tool is Travis CI

## Travis CI
- *travis CI* is a tool provided as webservice and is integrated into github/gitlab
- a configuration file has to be put into the repository called `.travis.yml`
```yml
language: python # specifies the language
python:
    - "2.7" # specifies the python version(s)
    - "3.7"
install:
    - pip install -r requirements # specifies the requirements
script:
    - python -m unittest discover # command to run the tests
```
- travis will run after every push
- the results can be seen in the travis account on their websit

# Linter
## Basics
- a linter is a tool that will go over the code and comment it
- the comments give tips and hints about refactoring possibilities and mistakes in the code
- they can even predict possible runtime bugs
- there are passive tools (give just a warning) and active tools (changing the code without warning)
- one of the common passive tools is ***flake8***
- one of the common active tools is ***black***

## Flake8
- flake8 comments the code in relation to the PEP8
- link to the flake8 doc: [link](https://flake8.pycqa.org/en/latest/user/options.html)
- is installable via pip
- to run over a file: `$ flake8 test.py`
- the output will be a list of warnings and errors
- e.g.
>
    test.py:6:1: E302 expected 2 blank lines, found 1
    test.py:23:1: E305 expected 2 blank lines after class or function definition, found 1
    test.py:24:20: W292 no newline at end of file
- flake8 is fully configurable with a config file stored in the project named `.flake8`

## Black
- is a unforgiving formatter
- cant be configurated
- enforces a specific code style
- installable via pip (needs python3.6)
- to run the tool: `$ black test.py`

# Further Information
- separate the tests in the root folder
- keep the test code separate from the package code
- name the test directory "*tests*"

# doubles
## Basics
- a test double is an object that exist just to satisfy calls without doing anything
- the double is called mock and the process is called mocking
- **definition**: "*the replacement of one or more function calls or objects with mock calls or object*"
- this technic aloows to get exactly defined states from systems to test units that are dependent on these
- often used if there is a network or db dependency

## Mock
- a mock function call returns predefined values without doing any processing => returns immediatly
- the mock function/object is entirely defined within the test
- python provides the `unittest.mock` module

## Mocking in Python
- is done by capturing an API function or object with `patch`
- `patch` intercepts a call and returns a `MagicMock` object
- this object can be set to return any value if their properties are correctly set

## Procedure of Mocking
1. Write the test for real API calls
2. determine which API calls has to be "*mocked*" (should be a small number, the test should not test the mock module)
3. patch the API calls within the test function
4. set up the `MagicMock` response
5. run the test