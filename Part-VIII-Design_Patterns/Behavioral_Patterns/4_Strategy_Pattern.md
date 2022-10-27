# 4 Strategy Pattern
## 4.1 Basics
- design a family of algorithms to a specific problem (each in own class)
- these objects have to be interchangeable so that at runtime the way to a solution can be switched to the most fitting approach
- the idea is to not has to double the size of a class when another functionality is added to it
- example would be: transportation selection in a navigator program, walking needs another implementation as driving by bike

## 4.2 Usecase
- in python there is seldom a usecase
- since there is no other data associated with the object a set of "top level domain functions" that are passed around would do the trick
- should be used when client code is in need of selecting from multiple imlpementations

## 4.3 General Design
- User -> Abstraction[interface] -> Implementation1 / Implementation2 / Implementation3 . . .
- e.g.
    1. Navigator class:
        - list routeStrategy
        - method build_route(PointA, PointB)
    2. RouteStrategy interface:
        - method build_route(PointA, PointB)
    3. Actual Implementations:
        - CarStrategy
        - PublicTransportStrategy
        - BikeStrategy

## 4.4 Python Implementation
### 4.4.1 Implementation
- nothing here to read
### 4.4.2 Example
````python
    from abc import ABC, abstractmethod
    from typing import list

    class Context:
        def __init__(self, strategy: Stratgy) -> None:
            self._strategy = strategy

        @property
        def strategy(self) -> Strategy:
            return self._strategy
        @strategy.setter
        def strategy(self, strategy: Strategy) -> None:
            self._strategy = strategy

        def do_buisness:logic(self) -> None:
            print("sorting is my buisness, but not sure how i will do it")
            result = self._strategy.do_algorithm(["a", "b", "c", "d"])
            print(",".join(result))

    class Strategy(ABC):
        @abstractmethod
        def do_algorithm(self, data: List):
            pass

    class ConcreteStrategyA(Strategy):
        def do_algorithm(self, data: List) -> List:
            return sorted(data)
    class ConcreteStrategyA(Strategy):
        def do_algorithm(self, data: List) -> List:
            return reverse(sorted(data))

    if __name__ == "__main__":
        context = Context(ConcreteStrategyA())
        context.do_buisness()
````
