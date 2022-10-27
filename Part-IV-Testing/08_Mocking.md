# Basics
- a mock-object substitutes and imitates an object for testing purpose
- through substituting an object the return values of a call to the object can be specified
- python provides `unittes.mock` as the standart built-in mocking library (since 3.3)

# unittest.mock
- `unittest.mock.Mock`: mock objects to substitute entire objects
- `unittest.mock.patch`: patch to substitute only an attribute of an object, can also import mock-objects into a scope (if a patch imorts a request object, it is automatically an mock-obj)
- `unittest.mock.MagicMock`: mock object that provides dunder methods

# Mock
- `unittest.mock.Mock` is the a base class to substitue
- a mock-object is instantiated with a class call e.g. `Mock()`
- the assigned mock object acceptes all attributes and method calls
    (it creates them at runtime)
- to substitute the `json` module json is assigned to the mock
    e.g. `json = Mock()` it will accept all calls
- all calls to the mock-object returns another mock object
- these objects can return how it was used or they are called
- with the call `unittest.mock.create_autospec([class to mock])` a mock-object is returned that have automatically all attributes from the given class

## methods of a Mock Object
- the mock object offers different assert statements that are elf explanatory
- if an assertion fails a `AssertionError` is raise
> MEANS that an extra assert statement will raise an error!
- `mock-obj.method.assert_called()`
- `mock-obj.method.assert_called_once()`
- `mock-obj.method.assert_called_with("{'key':'value'}")`
- `mock-obj.method.assert_called_once_with("{'key':'value'}")`
- `mock-obj.method.call_count`: return the amount of calls of the metod
- `mock-obj.method.call_args`: returns the arguments of the last call
- `mock-obj.method.call_args_list`: list of all calls of the method
- `mock-obj.calls`: list of all method calls to this object
- `mock-obj.method.called`: returns bool if it was called

## specifie a return value
- to specify a returnvalue call `mock-obj.method().return_value = value`
- e.g.
```python
from unittest.mock import Mock
import datetime

tuesday = datetime.datetime(year=2019, month=1, day=1)

datetime = Mock()
datetime.datetime.today.return_value = tuesday
# now everytime "datetime.datetime.today() is called the var tuesday ir returned"
```

## Mock Side-Effects
- the baehavior of a mock-obj function call can be altered through side-effects
- an example would be to create a side-effect that mimics a ping timeout for a network call
- `mock-obj.method.side_effect = [side-effect]`
- side-effect can be an iterable(returns every call the next item), an Exception, an object
- e.g.
```python
from unittest.mock import Mock
requests = Mock()

def log_request(self, url):
    # Log a fake request for test output purposes
    print(f'Making a request to {url}.')
    print('Request received!')

    # Create a new Mock to imitate a Response
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independence Day',
    }
    return response_mock

def test_get_holidays_logging(self):
    # Test a successful, logged request
    requests.get.side_effect = self.log_request
    assert get_holidays()['12/25'] == 'Christmas'
```

## Mock Attributes
- to set an attribute for a mock-obj just assign it
- e.g. `mock-obj.name = value`


# Patch
- patch does not mock a complete object, it mocks only an attribute
- used as decorator or in context with the `with` statement
    - a decorated function mocks the attribute during the function
    - a context statement mocks the attribute only for the context (nested code)
- patch returns an instance of magic mock
- to patch built-in function calls like "print()" you need to get the m from `builtins.[functioncall]

## decorator use
- to patch an object
- `@patch("[original_object]")`
- to patch an attribute
- `@patch.object([original_object], "[attribute to patch]", return_value=[return value])`

## context use
- to patch an object
- `with patch("[original_object]")`
- to patch an attribute
- `with patch.object([original_object], "[attribute to patch]", return_value=[return value])`

## example
```python
@patch.object("json", "dumps", True)
def test_sth():
    assert json.dumps()
```

# Spec / Autospec
- to change the behavior that a mock object creates attributes as needed during runtime
- a mock-obj can get a attribute list with the `spec` statement
- e.g. `mock-obj = Mock(spec=[["attribute_1"], ["attribute_2"]])`
- `create_autospec([original object])` will scan the original object and automatically adds all mock attributes of the object to the mock-obj