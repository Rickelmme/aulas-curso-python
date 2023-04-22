from __future__ import annotations

from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    rick = Person('Rick', 'Barreto')
    endereco_rick = Address('Londres', '205')
    rick.add_address(endereco_rick)

    filha_rick = rick.clone()
    filha_rick.firstname = 'Sophia'

    print(rick)
    print(filha_rick)
