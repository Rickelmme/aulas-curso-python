# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma aula? (tipo)
# Seu objeto é uma instância de sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Nome', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclasse é chamada e cria a nova classe
# __call__ da metaclasse é chamada com os argumentos e chama:
# __new__ da class com os argumentos (cria a instância)
# __init__ da classe com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclasse
# __new__(mcs, name, bases, dct) (Cria uma classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveria se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que preciso delas e não preciso de uma explicação
# sobre o porquê)."
# — Tim Peters (desenvolvedor principal do CPython)
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
            not callable (cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar') 

        return cls
    
    def __call__(self, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome') 

        return instancia

class Pessoa(object, metaclass=Meta):
    # falar = 123
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('FALANDO...')

p1 = Pessoa('Rick')
print(p1.attr)
p1.falar()