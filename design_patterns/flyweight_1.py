from __future__ import annotations

from typing import Dict, List


class Client:
    """ Context """

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic addresses data
        self.address_number: str
        self.address_details: str

    def add_address(self, addresses: Address) -> None:
        self._addresses.append(addresses)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(
                self.address_number, self.address_details
            )


class Address:
    """ Flyweight """

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourdhood = neighbourhood
        self._zip_code = zip_code

    def show_address(
            self, address_number: str, address_details: str
    ) -> None:
        print(
            self._street, address_number, self._neighbourdhood,
            address_details, self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight


if __name__ == "__main__":
    address_facyory = AddressFactory()

    a1 = address_facyory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='111-222-333-44'
    )
    a2 = address_facyory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='111-222-333-44'
    )

    rick = Client('Rick')
    rick.address_number = '150'
    rick.address_details = 'Casa'
    rick.add_address(a1)
    rick.list_addresses()

    zeca = Client('Zeca')
    zeca.address_number = '202'
    zeca.address_details = 'AP'
    zeca.add_address(a1)
    zeca.list_addresses()

    print(a1 == a2)
