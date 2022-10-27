# Basics
- integration tests are testing different components that have a relationship
- the test aims to reveal defects in the interfaces that these components use to communicate with each other
- integration test usually are conducted when the development of a functionality group is done an all components of this group passes the unit tests
- the aim should be to show that the system works as intendet despite being subdivised into components

# different kinds of integration tests
- the more units are grouped together for testing the more abstract the test system is
- therefor the integration tests are categorized into different groups, according to the composite of units they are composed of
- list of different integration test:
    - **functionsl test**: test if the endresult for a client is what a client might expect
    - **end-to-end test**: tests the real expierence of the user (uncover dependency issues like bugs in a specific os or browser)
    - **system test**: tests for real usage patterns, to verify that the system works as intended
    - **acceptance test**: tests for an implemented feature, the test aims to make sure that the implementation of a feature didnt break the system
- at the end the name of the test approach does not matter, just remember that **unit-tests** tests the implementation and that **functional tests** tests the behavior

# Integration Tests
- the unit tests should all pass, if not it isnt clear if a interface test fails because a unit does not work as expected or if it is a problem with the interface itself

# What to Test
- check only a single happy path per functionality
- if there are edge cases where unit tests aren working use integration tests aswell
- integration tests should test if data was created
- test important functionality (e.g. that an memo email is send to the customers)
- test restrictions (e.g. user with this username exists already)
- make sure that the system works with external dependencies

# Example Real World
- aircraft integration test:
    - correct interaction between some components => pressing the start button, the engine starts, the propeller rotating with the correct speed, plane stays on the ground
    - correct interaction with external components => check the embedded radio can communicate with a station
    - correct interaction between all involved components => show that the system as a whole works => the test crew starts the plane and fly with it