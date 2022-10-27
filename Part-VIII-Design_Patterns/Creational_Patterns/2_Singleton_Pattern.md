# 2 Singleton
## 2.1 Basics
- the singleton pattern allows only one object of a specific class to exist at the same time
- in python the singleton pattern is seen as "forcing someone into a specific mind set" and is not seen as the pythonian way

## 2.2 Usecase
- often used as manager object

## 2.3 General Design
- the constructor is made private(not callable from the outside)
- a specific method to receive the object is provided
- this method instanciates the object the first time its called
- every other call will lead to a reference to this instance

## 2.4 Python Implementation
### 2.4.1 implementation
- because there are no private constructors in python the dunder method ``__new__`` could be used to create a singleton pattern
- if really in need of a singleton pattern, use "module-level-variables"(i.e. create an instance of a normal class and assign it to a variable at the modul level and pass this around)

### 2.4.2 Example
````python
    # singleton example
    class SingletonClass:
        _singleton = None
        def __new__(cls, *args, **kw):
            if not cls._singleton:
                cls._singleton = super(SingletonClass, cls).__new__(cls, *args, **kw)
            return cls.singleton
````