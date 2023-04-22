# Exercicício - unir listas
# crie uma função zipper (como zipper de roupa)
# O trabalho dessa função será unir duas
# listas na ordem
# Use todos os valores da lista menor
# Ex:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# SOLUÇÃO 1
def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i]) for i in range(intervalo)
    ]
   
   
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))


# SOLUÇÃO 2  usando a lista menor
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))


# SOLUÇÃO 2   usando a lista maior
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))