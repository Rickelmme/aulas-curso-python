# append  -> Adiciona um item ao final
# insert  -> Adiciona  item ao índice escolhido
# pop  -> Remove do final ou do índice escolhido
# del  -> Apaga um índice
# clear  -> Limpa a lista
# extend  -> Estende a lista
# +  -> concatena listas

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

