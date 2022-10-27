# 5 Fleyweight Pattern
## 5.1 Basics
- is a memory optimization pattern
- mostly implemented after a sysem shows memory related problems
- e.g. a car sales/management program, most of the cars have similar features, it can be more efficient to share common features among cars and only create new ones when nesseccary
- BUT WHEN IN NEED OF DEALING WITH A LARGE AMOUNT OF OBJECTS USE ``__slots__`` the flyweight pattern is not that readable and maintainable!

# Usecase
- when a program shows problems to fit into the ram(i.e. particle system in a shooter can easily use massive amounts of ram)

# General Design
- work like a singleton
- an object jsut gets a reference to specific features instead of saving it in its own memory separat

# Python Implementation
- the weakref module provides functionality for this pattern