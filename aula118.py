# Problema dos parâmetros mutáveis em funções python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
cliente1 = adiciona_clientes('Rick', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
adiciona_clientes('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)


print(cliente1)
print(cliente2)
print(cliente3)