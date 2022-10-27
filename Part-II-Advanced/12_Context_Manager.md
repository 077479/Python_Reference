# 12 Context Manager
- python provides 2 special methods that are called through the ``with`` statement
- the ``__enter__`` method and the ``__exit__`` method
- ``__enter__`` the enter method is run before entering the nested codeblock
- ``__exit__`` the exit method is run before exiting the nested codeblock
- every object that provides this method works with the ``with`` statement
- these methods are dunder methods that can freely be implemented