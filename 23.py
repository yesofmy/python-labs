from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    Інтерфейс Builder визначає методи для створення різних частин продукту.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_size(self, size: str) -> None:
        pass

    @abstractmethod
    def add_milk(self, milk_type: str) -> None:
        pass

    @abstractmethod
    def add_syrup(self, syrup: str) -> None:
        pass

    @abstractmethod
    def add_espresso_shot(self) -> None:
        pass


class CoffeeBuilder(Builder):
    """
    Конкретний будівельник для створення кави.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Coffee()

    @property
    def product(self) -> Any:
        result = self._product
        self.reset()
        return result

    def set_size(self, size: str) -> None:
        self._product.size = size

    def add_milk(self, milk_type: str) -> None:
        self._product.milk = milk_type

    def add_syrup(self, syrup: str) -> None:
        self._product.syrup = syrup

    def add_espresso_shot(self) -> None:
        self._product.espresso_shots += 1


class Coffee:

    def __init__(self) -> None:
        self.size = None
        self.milk = None
        self.syrup = None
        self.espresso_shots = 0

    def list_parts(self) -> None:
        parts = [
            f"Розмір: {self.size}",
            f"Молоко: {self.milk}",
            f"Сироп: {self.syrup}",
            f"Шоти еспресо: {self.espresso_shots}",
        ]
        print(f"Кава: {', '.join(filter(None, parts))}")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def make_latte(self) -> None:

        self.builder.set_size("Середній")
        self.builder.add_milk("Звичайне молоко")
        self.builder.add_espresso_shot()

    def make_cappuccino(self) -> None:

        self.builder.set_size("Малий")
        self.builder.add_milk("Мигдалеве молоко")
        self.builder.add_syrup("Шоколадний")
        self.builder.add_espresso_shot()

    def make_custom_coffee(self, size: str, milk: str, syrup: str, shots: int) -> None:

        self.builder.set_size(size)
        self.builder.add_milk(milk)
        if syrup:
            self.builder.add_syrup(syrup)
        for _ in range(shots):
            self.builder.add_espresso_shot()


if __name__ == "__main__":
    director = Director()
    builder = CoffeeBuilder()
    director.builder = builder

    print("Латте: ")
    director.make_latte()
    builder.product.list_parts()

    print("\nКапучино: ")
    director.make_cappuccino()
    builder.product.list_parts()

    print("\nКастомна кава: ")
    director.make_custom_coffee(size="Великий", milk="Мигдалеве молоко", syrup="Ванільний", shots=2)
    builder.product.list_parts()