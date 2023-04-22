from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    veiculos_disponiveis_zona_norte = [
        'carro_luxo', 'carro_popular', 'moto_popular', 'moto_luxo'
    ]
    veiculos_disponiveis_zona_sul = [
       'carro_popular', 'moto_popular'
    ]

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
