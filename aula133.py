# Encapsulamento (modificadores de acesso: público, protegido, privado)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem sublinhado) = público
#       pode ser usado em qualquer lugar
# _ (um sublinhado) = protegido
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois sublinhados) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

f = Foo()
# print(f.public)
print(f.metodo_publico())
print(f._Foo__metodo_private())