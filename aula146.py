# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma execeção da linguagem.
# A recomendação da doc é herdar de Exceptions.
# Notas das exceções em Python (add_notes, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comun colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em diferente (3.11.0)
class MyError(Exception):
    pass

class MyOtherError(Exception):
    pass

def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = MyOtherError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error