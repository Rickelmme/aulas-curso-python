from typing import (Callable, Dict, Iterable, List, NewType, Sequence, Tuple,
                    Union)

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = True
string: str = 'Rickelmme'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[str, int]] = [1, 2, 3, 'Rickelmme']
# tupla: Tuple = (1, 2, 3, 'Rickelmme')
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Rickelmme')

# Dicionários e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]

pessoa1: Dict[str, Union[str, int]] = {
    'nome': 'Rickelmme', 'sobrenome': 'Barreto', 'idade': 18
}
pessoa2: MeuDict = {
    'nome': 'Rickelmme', 'sobrenome': 'Barreto', 'idade': 18, 'lista': [1, 2]
}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(12345)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está passando...')


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))

print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
