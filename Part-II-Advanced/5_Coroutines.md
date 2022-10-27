# 5 Coroutines
## 5.1 basics
- mostly used with the asyncio module, otherwise seldom usecases
> 
    coroutines are a theoretical idea in computer science and are considered a more general version of generators (there is a relation between functions/subroutines and coroutines) => functions are a kind of coroutines, generators are a kind of coroutines, and there are coroutines that are neither
- coroutines function like generators, but instead of just returning a value, it is possible to insert a value into the generator object and process it til the next yield
- the magic word is "send" (in fact every generator has this interface)
- what happens is:
    0. the gnerator has to be created and activated with a first "next" statement
    1. yield occurs and the generator pauses
    2. "send()" is called on the generatorm, it wakes up
    3. the value "send in" is assigned to the left of the yield statement
    4. the generator continues to process til the next yield
- when chaining up coroutines/generators are pretty dificult to manage all the states between them (especially when accounting contextmanager), therefor the asyncio module has some clever functionality wrapped around it

## 5.2 example
```python
def coroutine_test():
    val = 0
    while True:
        increment = yield val
        val += increment
gen = coroutine_test()
gen.next() # returns 0
gen.send(2) # returns 2
gen.send(3) # returns 5
```
- what happens is:
    0. the "next()" call activates the generator
    1. it goes to the first "yield" which "yields"(=returns) the value assigned to "val" and the generator is paused
    3. the "send" wakes the generator
    4. the value "send" to the generator is assigned to the var "increment"
    5. the generator begins to execute the code til the next yield statement (updates the val variable)
    6. the mentioned "yield" command "yields"(=returns) the value assigned to "val" and the generator is paused
- conclusion should be => avoid using this outside of use with asyncio