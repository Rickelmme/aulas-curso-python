""" Calculadora com while """

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - / *): ')
   
    numeros_validos = None
    num_1float = 0
    num_2float = 0

    try:
        num_1float = float(n1)
        num_2float = float(n2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos dos números digitados são invalidos.')    
        continue

    operadores_permitidos = '+ - / *'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1float}+{num_2float}=', num_1float + num_2float)
    elif operador == '-':
        print(f'{num_1float}-{num_2float}=', num_1float - num_2float)
    elif operador == '/':
        print(f'{num_1float}/{num_2float}=', num_1float / num_2float)
    elif operador == '*':
        print(f'{num_1float}*{num_2float}=', num_1float * num_2float)
    else:
        print('Não deveria chegar aqui.')

    sair = input('Quer sair ? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break