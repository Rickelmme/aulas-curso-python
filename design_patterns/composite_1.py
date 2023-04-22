from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """ Composite """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    """ Leaf """
    camiseta_1 = Product('camiseta_1', 80)
    camiseta_2 = Product('camiseta_2', 100)
    camiseta_3 = Product('camiseta_3', 30)

    """ Composite """
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta_1)
    caixa_camisetas.add(camiseta_2)
    caixa_camisetas.add(camiseta_3)
    # caixa_camisetas.print_content()

    """ Leaf """
    smartphone_1 = Product('smartphone_1', 2500)
    smartphone_2 = Product('smartphone_2', 800)
    smartphone_3 = Product('smartphone_3', 4500)

    """ Composite """
    caixa_smartphones = Box('Caixa de smartphone')
    caixa_smartphones.add(smartphone_1)
    caixa_smartphones.add(smartphone_2)
    caixa_smartphones.add(smartphone_3)
    # caixa_smartphones.print_content()

    """ Composite """
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print()
    print('Valor total =', caixa_grande.get_price())
