# 2 Adapter Pattern
## 2.1 Basics
- performing a translation between interfaces that wouldnt work normally together
- these classes are often called "Adapter"

## 2.2 Usecase
- when a needed object cant be changed a "adapter" class can be used to adress the differences
- converting arguments to different formats, or arranging a specific order of arguments, or just passing data through different interfaces, or supplying default arguments

## 2.3 General Design
- similar to a simplified decorator

## 2.4 Python Implementation
- a way to go could be to inherit from a class that provides the needed adapter functionality
- e.g. a class that needs a weird kind of format for a date, the datetime.date class could be inherited from and a method can be added to return this specific format
- but its normally more clear and better to maintain/read with an "adapter" class
