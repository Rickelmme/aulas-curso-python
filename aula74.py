"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Gaby', 'Helena']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))



# Praticando

# def comprimento(frase):
#     def comprimentar(name):
#         return f'{frase}, {name}'
#     return comprimentar

# comprimento_ola = comprimento('Olá')
# comprimento_tchau = comprimento('Tchau')

# for name in ['Rick', 'Julia', 'Gaby', 'Ana']:
#     print(comprimento_ola(name))
#     print(comprimento_tchau(name))