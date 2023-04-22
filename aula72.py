# Multiplica todos os argumentos não nomeados recebidos


def multiplicar(*args):
    total = 1
    for number in args:
        total *= number
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

# --------------------------------------------

# PAR ou ÍMPAR usando return 

def par_impar(number):
    mult_de_dois = number % 2 == 0

    if mult_de_dois:
        return f'{number} é par'
    return f'{number} é ímpar'

print(par_impar(9))
print(par_impar(7))
print(par_impar(10))
print(par_impar(4))