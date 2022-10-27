# 3 Facade Pattern
## 3.1 Basics
- the facade pattern provides a simplified interface to a more complex library or framework or other complex functionality
- if nesseccary the complex functionality can be accessed from the outside

## 3.2 Usecase
- if you need only a specific set of an complex framework its often better to create a "fassade" for the complex framework in order to get a more simple interface

## 3.3 General Design
- the "facade provides convinient access to a particular part of a subsystems functionality"
- an additional facade class can be created to prevent polluting a single facade with unrelated features
- a client then uses the facade instead of the complex subsystem(i.e. the client doesnt have to dive into the framework and initialize all the objects in the right order to get a single functionality going)

## 3.4 Python Implementation
- nothing to read here