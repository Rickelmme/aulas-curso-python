# raise = lançando execeções (erros)

def nao_aceito_0(d):
    if d == 0:
        raise ZeroDivisionError('NN PD DIVIDIR POR 0')
    return True

def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" Deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceito_0(d)
    return n / d


print(divide(8, '0'))