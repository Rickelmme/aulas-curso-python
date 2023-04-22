from __future__ import annotations

from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    """ Subject Interface """
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    """ Real Subject """

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # Simulando requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulando requisição
        return {
            'cpf': '111.111.111.11',
            'rg': '111222333444'
        }


class UserProxy(IUser):
    """ Proxy """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        # Esses objetos ainda não existem
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cache_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == "__main__":
    rick = UserProxy('Rick', 'Barreto')

    print(rick.firstname)
    print(rick.lastname)

    # 6 segundos
    print(rick.get_all_user_data())
    print(rick.get_addresses())

    # Responde instantaneamente
    print('CACHE DATA:')
    for i in range(10):
        print(rick.get_addresses())
