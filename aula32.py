# Exercicio par ou impar

'''
numero_int = (input('Digite um número inteiro: '))

if numero_int.isdigit():
    numero = int(numero_int)
    par_impar = numero % 2 == 0
    par_impar_texto = 'ímpar'
    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero} é {par_impar_texto}') 
else:
    print('Você não digitou um número inteiro')
'''

# Exercicio horario 

'''
horario = input('Que horas são ? ')

try:
    hora = int(horario)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor digite um número inteiro')
'''

# Exercicio nome

'''
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome < 1:
    if len(nome) <= 4:
        print('Seu nome é muito curto')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal')
    elif len(nome) > 6:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
''' 
