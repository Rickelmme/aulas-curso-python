# dataclasses - O que são dataclasses ?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__(), (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclsses são syntax sugar para criar classes normais.
# Foi descrito na PEP 5557 e adicionado na versão 3.7 do Python.

from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    print(p1)
