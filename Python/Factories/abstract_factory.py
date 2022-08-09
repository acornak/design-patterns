"""
Design pattern: Abstract Factory
"""

from abc import ABC
from enum import Enum, auto
from typing import Any


class HotDrink(ABC):
    """
    Abstract Hot Drink class
    """

    def consume(self) -> None:
        """
        Consume
        """


class Tea(HotDrink):
    """
    Tea class
    """

    def consume(self) -> None:
        """
        Consume
        """
        print("This tea is delicious")


class Coffee(HotDrink):
    """
    Coffee class
    """

    def consume(self) -> None:
        """
        Consume
        """
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    """
    Hot Drink abstract factory class
    """

    def prepare(self, amount: int) -> Tea | Coffee:
        """
        Prepare hot drink
        """


class TeaFactory(HotDrinkFactory):
    """
    Create tea
    """

    def prepare(self, amount: int) -> Tea:
        """
        Prepare hot tea
        """
        print(f"Put in tea bag, boil water, pour {amount} ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    """
    Create coffee
    """

    def prepare(self, amount: int) -> Coffee:
        """
        Prepare hot coffee
        """
        print(f"Grind some beans, boil water, pour {amount} ml, enjoy!")
        return Coffee()


def make_drink(beverage: str) -> Tea | Coffee | None:
    """
    Return correct drink
    """
    if beverage == "tea":
        return TeaFactory().prepare(200)
    if beverage == "coffee":
        return CoffeeFactory().prepare(200)
    return None


class HotDrinkMachine:
    """
    Hot Drink Machine class
    """

    class AvailableDrink(Enum):
        """
        List of available drinks
        """

        COFFEE = auto()
        TEA = auto()

    factories: list[str | Any] = []
    initialized = False

    def __init__(self) -> None:
        """
        Constructor
        """
        if not self.initialized:
            self.initialized = True
            for hotdrink in self.AvailableDrink:
                name = hotdrink.name[0] + hotdrink.name[1:].lower()
                factory_name = name + "Factory"
                # pylint: disable=fineval-used
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        """
        Make drink
        """
        for factory in self.factories:
            print(factory[0])

        selected = int(input(f"Please pick a drink (0-{len(self.factories) - 1})"))
        amount = int(input("Specify amount: "))
        return self.factories[selected][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.make_drink()
