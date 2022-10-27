# 2 Flow Control
# 2.1 Break, Continue, Pass
- "break" and "continue" keywords can alter the behaviour of loops

## break:
- terminates a loop // only the construct in which it is, in nested constructs only the inner construct will be ended
- outside of a loop the break statement will raise a SyntaxError (break outside of loop)

## continue:
- used to skip the rest of the "loop" and start it over // the rest of the codeblock after the continue will not be executed, it starts right at the beginning of the loop with the evaluation

## pass:
- pass is a "null" statement it does nothing
- its used as placeholder to lay out structures like objects // a declared codeblock whitout a statement will raise an exception (EOF unexpected end of line)

# 2.2 If/Else
## If
- the ''if else'' statement is provided to control the program flow, the "if statement" evaluates a boolean statemen("True" or "False") and if the result is True the "codeblock" within the if statement is processed
- if the result of the evaluated statement is a numeric that results other than 0 it is considered as "True", a result of 0 will be considered as "False"
- the result ''None'' will be cosnidered as "False"
- the if block is created by the keyword ''if''
- e.g:
```python
if [boolean statement]:
    print(will only be executed when the statement above is considered true)
```

## Else
- to create an "either or" statement with the "if" construct an "else" statement can be added to the "if block"
- the else block will be processed only if the evaluation of the boolean statement is False
```python
if [boolean statement]:
    print("will only be executed when the statement above is True")
else:
    print("will only be executed if the statement above is False")
```

## Elif
- for the evaluation of several boolean statements the if block can be supplemented by a ''elif [boolean statement]'' statement
- there can be unlimited "elifs"
- but be aware nested if statements arent good practicee (i.e. if statements in if statements)
invert the ifs:
- it is good practice to get rid of dangling if statments with inverted if statements, see "9.2"

# 2.3 For Loop
- in python there is no "classic" for loop
- the "for" keyword generates an "iterator" object that iterates through items in an interable object
- i.e. the for loop returns elements from datastructures (or any object that has the iterate interface) one after another for processing
- a "classic" for loop can be generated with the range function (Advanced Topics => Functions To Know => Range)
- the loop continues til the last item is reached
- the for loop can have an extra else, when the loop is stopped with a "break" the else wont be processed (imagine a for loop goes over a list and searches a specific item, if it finds it a break could end the loop, but if the item isnt found the for loop just ends, and the processing of the code goes on, to do a "that has to be done after the for loop find nothing sort of situation an else statement can be added to the for loop)

> the for loop is implemented as a while loop that has "True" as argument and is stopped by an exception

# 2.4 While Loop
- a loop that evaluates a "boolean statement" and if "True" the underlying codeblock will be processed
- after every turn(one processing of the entire codeblock) the boolean statement is evaluated again and if the statement is agian true the codeblock is run again

# 2.5 Switch
- in python there is no switch statement
- if necessary a switch statements can be realized with the evaluation of an argument against a dictionary mapping
```python
    def switch_demo(argument):
        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
    print(switcher.get(argument, "Invalid month"))
```