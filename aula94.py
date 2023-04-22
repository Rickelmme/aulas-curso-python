# try, execpt e finally

try:
    print('ABRIR ARQUIVO')
    8 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
else:
    print('NÃO DEU ERRO')
finally:
    print('FECHAR ARQUIVO')