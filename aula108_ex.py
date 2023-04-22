# Usando a lista menor
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4,]

d = [
    lista_a + lista_b for lista_a, lista_b in zip(lista_a, lista_b)
]

print(d)

# Usando a lista maior
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4,]

d = [
    lista_a + lista_b for lista_a, lista_b in
    zip_longest(lista_a, lista_b, fillvalue=0)
]

print(d)