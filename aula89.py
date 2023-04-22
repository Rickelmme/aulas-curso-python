# dir, hasattr e getattr em Python
string = 'Rick'
metodo = 'upper'

if hasattr(string, metodo):
    print('Exite upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
