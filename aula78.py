# s1 = set('Rick')
# s1 = set() # Vazio
# s1 = {'Rick', 1, 2, 3} # Com dados

# l1 = [1, 2, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

s1 = set()
s1.add('Rick')
s1.add(1)
s1.update(('Olá, Mundo!', 1,2,3,4))
# s1.clear()
s1.discard('Olá, Mundo!')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # União - Une
s3 = s1 & s2  # Intersecção - Itens presentes em ambos
s3 = s1 - s2  # Diferença - Itens presentes apenas no set da esquerda
s3 = s1 ^ s2  # Diferença simétrica - Itens que não estão em ambos
print(s3)
