# 6 Closures
- a closure is a variable that is bind to a function/method in order to store it for later use
- criteria to create a closure
	1. a nested function is neccessary
	2. the nested function has to refer to a value within the enclosing function
	3. the enclosing function has to return the nested one
- often used when a function is too much for little functionality
```python
def print_msg(msg):

	def printer()
		print(msg)

	return printer

closure_var = print_msg("hello")
del print_msg
closure_var() # returns the beforehand saved functionality
```