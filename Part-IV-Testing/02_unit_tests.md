# Basics
- a unit is the smallest testable component that participates in the program
- this means a unit should reflect a functionality, this can be a single class, or a top level domain function, or ...
- units are distinct into two different categories:
    - **solitary unit**: a functionality that does not depend on other functionalities
    - **sociable unit**: a functionality that does depend on other functionalities (i.e a function that calls another function for like a multiplyer that calls the addition functionality and adds the base as many times to itself that are given)

# Unit Tests
- method that looks at the smallest parts of software and verifies their correct work
- goal is to verify that each part of the code works as intended
- each small piece of functionality is tested independently
- the corresponding unit test should be run everytime we change code in a unit

# What to Test
- there should be tests for all possible input data
- e.g. for an area property in a rectangle class there should be tests for:
    - if values of rectangle are present
    - area not empty
    - area not negative => correct return val or exception should be raised
    - test correct area for different vals