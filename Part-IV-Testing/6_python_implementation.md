# Assert Statement:
- python provides for testing the assert statement
- a test of a *sum function* would look like: `assert sum([1,2,3]) == 6`
- the assert statement only gives feedback if a test fails, (raises assertion error)
- this isnt practicable, because an raised error stops the execution, therefor ***testrunner*** are used

> it is convention that test files start with "*test_*", usually python test runner searching for this pattern

# Python Test Frameworks
- there are tons of different test frameworks which provides their own special functionality
- the most common ones are:
    - **unittest** (built-in)
    - **pytest**
    - **nose** or **nose2**

# Pytest
## Basics
- is a convinience testframework for python
- uses the python built-in assert method
- is open to community development through plugins => has a rich ecosystem to test nearly every existing scenartio

## Runner
- runner searches for files called `test_...` and executes all functions called `test_...`
- runner is started with `py.test <directory/file>` => /root$ py.test tests
    - if no argument is given it searches for a directory called tests and executes the content tests
- executes unittest tests aswell

### Filter
- pytest can filter:
    - **names**: `-k <name>` lets pytest only execute files with the <name> in its name
    - **directrie**: a specific dir can be given as argument
    - **category**: `-m cat` executes only tests of a specific category(functions can be marked)

## Parametrization
- pytest provide markers to categorize tests
- pytest can run different categories together
- often used to categorize dependenies like DBs or WebRes
- the markers have to be described in the pytest.ini file
- e.g.
>
    # pytest.ini
    [pytest]
    markers=
        category_1: description
        category_2: description
    
    # test_something.py
    import pytest

    @pytest.mark.category_1
    def test_me_now():
        asert something
- the marking happens through decorators
- e.g.: `@pytest.mark.<name>` 
- pytest returns a list of aviable markers with `$pytest --markers`
- categories can be choosen with the `-m` option
- e.g. `pytest -m web_tests`
- excluding is also possible e.g. `pytest -m "not web_tests"`
- pytest built-in markers are:
    - **skip**: skips the test unconditionally (without a boolean statement)
    - **skipif**: skips a test if the expression passed to it evaluates to True
    - **xfail**: indicates that the test is expected to fail
    - **parametrize**: creates multiple versions of the tests with different values

## Parametrization
- to test different values on the same functionality pytest rovides the **parametrize** marker
- within the **parametrize** decorator a list of parameters are defined and a with it decorated test function will work through them
- avoids to create 20 different tests to test 20 different values on the same funcitonality
- the syntax is: `@pytest.mark.parametrize("name_of_container", [list, of, tuples or single values])`
- e.g.
```python
import pytest

@pytest.mark.parametrize("test_strs, expected_results", [("", True), ("a", True), ("Bob", False), ("Do geese sneeze", False)])
def test_if_geese_sneeze(test_strs, expected_results):
    assert do_geese_sneeze(test_str) == expected_results
```

## Benchmark
- pytest offers a built-in benchmark
- it can automatically record and report the duration of each run test
- this can be provoked with the `--durations=n` option
- `n` determines which tests should be displayed
- `n` the slowes `n` tests will be reported
- for verbose output of the durations the `-vv` flag is needed
- be aware if there are tests that create a teststructure their time will be increased in relation to theese that just use then the teststructure
> think of `pytest_django` plugin, the first test with the marker **django_db** will create the database every following test will just access it, this will show in the time reported

## Pytest Ini
- the `pytest.ini` is one of different ways to cofigure the behavior of pytest
> others could be `pyproject.toml`, `tox.ini`, `setup.cfg`
- link to the doc of pytest config: [link](https://docs.pytest.org/en/6.2.x/reference.html#configuration-options)
- the `pytest.ini` has to be stored in the root-test directory
- the pytest searches only in the called directory for the .ini
- means if `py.test` is called from root dir, the ini has to be there

## Output
- output is slightly different from unittest
- **e.g.**
>
    ============================= test session starts =============================
    platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
    rootdir: /home/olischer/Lab/Python/env/env_pytest/app
    collected 2 items                                                             

    tests/test_basics.py .F                                                 [100%]

    ================================== FAILURES ===================================
    ______________________________ test_always_fail _______________________________

        def test_always_fail():
    >       assert False
    E       assert False

    tests/test_basics.py:10: AssertionError
    =========================== short test summary info ===========================
    FAILED tests/test_basics.py::test_always_fail - assert False
    ========================= 1 failed, 1 passed in 0.02s =========================
- the first line after the system shows tests outcomes like unittest
    - `.`: passed test
    - `F`: failed test
    - `E`: unexpected exception exception was raised

## Fixtures
- pytest fixtures are functions that create data
- they are modular (can be imported, can itself import and can depend on other fixtures)
- they are used as decorator 
- the decorated function is then given as parameter to the test function that needs the data
- **e.g.**
```python
@pytest.fixture
def example_fixture():
    with open("json_file", "r") as file:
        return json.load(file)

def test_fixture(example_fixture):
    assert example_fixture["name"] == "john"
```

## Scaling Fixtures
- if tests require slightly variations of data a fixture isnt the right solution
- if the fixture structure gets more complex => own fixture structure
- in pytest a `conftest.py` allows special configuration of fixture files
- pytest searches for a `conftest.py` file in each directory
- the there defined or imported fixtures are aviable in all adjacent or sub modules

## MonkeyPatching with pytest
- pytest provides the functionality to catch and react to API calls
- the fixture decorator is used
- the fixture has to import `monkeypatch`
- `monkeypatch.setattr(<module>, <function>, <return_val>)`
```python
# conftest.py
import pytest, requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kw: stunted_get())
```
- the `autouse=True` modifyer activates this rerouting of the `request.get()` call everytime pytest is started
- another valid usecase is to restrict acces to certain ressources to specific categories of test
- the `pytest-django` plugin does that with the DB access
- only tests marked with "*django_db*" can create or access the DB others will raise an Error

## Common used Plugins
- link to the full list of aviable plugins: [link](https://docs.pytest.org/en/latest/reference/plugin_list.html)
- **pytest-randomly**: forces the tests to run in random order
- **pytest-cov**: offers the `--cov` to report the testcoverage or the implemented code
- **pytest-django**: provides useful fixtures for tests for the django_db framework

# unittest
## Basics
- from JUnit inspired test-framework
- provides a framework aswell as a test runner
- link to the unittest doc: [link](https://docs.python.org/3/library/unittest.html)
- is built-in in python since 2.2
- there are different versions of unittest for python2 and python3
- the normal import of unittest will give access to the python3 version
- for the python2 version the import has to be `import unittest2`
- **requirements:**
    - each test has to be put in methods in a class derived from `unittestTestCase`
    - the use of a series of special assertion methods (the normal "assert" command can be used)

### example sum function:
```python
import unittest

class TestSum(uunittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum([1,2,3]), 6)
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,3)), 6)

if __name__ == "__main__":
    unittest.main()
```

## Assertion Methods on TestCase class
- `.assertEqual(a,b)`: a==b
- `.assertTrue(x)`: bool(x) is True
- `.assertFalse(x)`: bool(x) is False
- `.assertIs(a,b)`: a is b
- `.assertIsNone(x)`: x is None
- `.assertIn(x)`: a in b
- `.assertIsInstance(x)`: isinstance(a,b)
- `.assertIsNot(a,b)`: not(a is b)
- `.assertIsNotNone(x)`: not(x is None)
- `.assertNotIn(x)`: not(a in b)
- `.assertIsNotInstance(x)`: not(isinstance(a,b))
- `.assertRaises(Error)`: Error == raised error

## Test Runner
- for unittest there are different ways to start the test runner
    1. a test runner can be started manually with `unittest.main()`
        - this will execute all test methods from classes derived from `unittest.TestCase` that are named "test_..."

    2. another way is to call the module and give the test file as argument: `python -m unittest <test_modul>`
        - this will do the same as `unittest.main()`
    3. another way is to call the discover command on unittest
        - in "discover mode" the test engine will search a given directory (including subdirectories) for `.py` files starting with "test"
        - option for the command "discovery":
        - **-v**: verbose, more output
        - **-s**: source gives discover a directory to go through
        - **-k str**: will only run test files that contain "str" in the name
        - e.g.: `py -m unittest discover ./test/ -v` or `py -m unittest discover ./test/ -k "acceptance"`
> the unittest runner will go through the tests in alphabetically order!
> be aware that the `unittest.main()` testrunner ONLY runs through the namespace and looks for subclasses of unittest.testcase with a name leading with "test_..." and in these classes only the methods named "test_..." will be executed!

## Test Case
- in unittest each test-case is declared by subclassing from the ``unittest.TestCase`` class
- and a method called ***test*** contains the actual action to:
    1. set a system to a(in the class) defined precondition
    2. run through the actions
    3. to check the postconditions
- after the tests are confirmed the system is set into the original state
- has a special method called `setUp()`
    - this method is called before any test of the class is run
    - is used to get fixtures in place

## e.g.
```python
import unittest

class TestClass(unittest.TestCase):
    def test_one(self):
        pass

if __name__ == "__main__":
    unittest.main()
```

##  unittest discover
- unittest has an option called discover

## Output
>
    [olischer@coldwell learn]$ py -m learn_test.test.test
    F.
    ======================================================================
    FAIL: test_list_fraction (__main__.TestSum)
    test for sum of a list of fractions
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/home/olischer/Lab/Python/learn/learn_test/test/test.py", line 20, in test_list_fraction
        self.assertEqual(result, 1)
    AssertionError: Fraction(9, 10) != 1

    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    FAILED (failures=1)
- the first line shows the result of the tests (`F`: fail, `.`: pass)
- Fail: shows the ***method that failed*** and in brackets the `__name__.object`
- the traceback of the failing line
- the detail of the assertion
<br>
<br>

## setup / teardown
- a setUp as object method method wil be called before every test in the class
- a setUplass as class method method wil be called once when initiating the class
- a tearDown as object method method wil be called after every test in the class
- a tearDownClass as class method method wil be called after every test in the class
```python
class Example(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    def setUp(self):
        print("setUp")
    
    def test_1():
        print("test_1")
    
    def test_2():
        print("test_1")
    
    def tearDown(self):
        print("tearDown")
    
    @classmethod
    def tearDown(cls):
        print("tearDownClass")
```


# Nose
- nose is a testrunner to make the unittest syntax more readable
- nose were abondoned and a fork "*nose2*" was created
- full support of unittests



# example test_class
```python
########## - Imports - ##########
import unittest, pytest
from tests import conftest

########## - Logic - ##########
class TestSyntax(unittest.TestCase):
    
    ########## - Setup Teardown - ##########
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    ########## - Tests - ##########
    
    @pytest.mark.skip
    def test_(self):
        pass
```