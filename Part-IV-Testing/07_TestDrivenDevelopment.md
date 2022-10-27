#  Test Driven Developmnnt
- the "*Test Driven Development*" approach states that writeing the tests before the code forces the dev to reason about the requirements
- which lead to expressing the requirements in a strict, well-defined and clear way within the implementation
- the idea of the process is to:
    1. first define the requirements (e.g. an addition function has to add two numbers)
    2. then the tests are creaed to test if the requirement is met e.g. `assert addion()==5`
    3. then the test is run one time to confirm the test works
    4. then the code is implemented to satisfy the requirement
    5. then the code goes through a revision phase and is refactored
    6. after imporving the code the test is run again to see if the changes have broken the requirement
    7. if other use cases come up the tests are refactored and improved aswell
- unit tests are the foundation of TDD therefor the ***Test Pyramid*** model works well with it
<br>
<br>

# Basics
- first it is sugested to create a todo list, during development make TODOs what should be improved, supported, replaced
- tehre are two approaches for TDD 
    1. **top down**: the most complex first then the others in order
    2. **down top**: the least complex first then the others in order


# Primary Acceptance Test
- a this is what i want to achieve test
- exposes the components needed to create the functionality

> 
    Testing is so important to good software development that there’s even a software development process based on testing, Test Driven Development (TDD). Three rules of TDD proposed by Robert C. Martin are:

        You are not allowed to write any production code unless it is to make a failing unit test pass.
        You are not allowed to write any more of a unit test than is sufficient to fail, and compilation failures are failures.
        You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

    The key idea of TDD is that we base our software development around a set of unit tests that we have created, which makes unit testing the heart of the TDD software development process. This way, you are assured that you have a test for every component you develop.