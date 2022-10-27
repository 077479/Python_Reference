# 5 Observer Pattern
## 5.1 Basics
- a "subject"(also called publisher) notifies a or several "subscribers" when something noteworthy happens
- an real world example would be a store that calls a customer to inform about the arrival of a new product

## 5.2 Usecase
- a typical usecase is eventhandling e.g. a custom button that let some clients hook some custom code to it
- when object(s) must observe another object for a limited time or in specific circumstances

## 5.3  General Design
- the "subject" gets an array of references to objects that should be notified on a specific circumstance
- plus functionality to manage this list

## 5.4  Python Implementation
````python
    class Inventory:
        def __init__(self):
            self.observers= []
            self._product = None
            self._quantity = 0

        def attach(self, observer):
            self.observers.append(observer)

        @property
        def product(self):
            return self._product
        @product.setter
        def product(self, value):
            self._product = value
            self._update_observers()

        @property
        def quantity(self):
            return self._quantity
        @quantity.setter
        def quantity(self, value):
            self._quantity = value
            self._update_observers()

        def _update_observers(self):
            for observer in self.observers:
                observer() # the observers have to implement "__call__" to process the update

    class ConsoleObserver:
        def __init__(self, inventory):
            self.inventory = inventory
        def __call__(self):
            print(self.inventory.product)
            print(self.inventory.quantity)

    # create the objects
    i = Inventory()
    c1 = ConsoleObserver()
    c2 = ConsoleObserver()
    # add the subscriber to the publisher
    i.attach(c1)
    i.attach(c2)
    # add new product to publisher
    i.product("SomeCoolGadget")
    i.quantity("5")
````