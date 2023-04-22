# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def My_Open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:    
        print('Fechando arquivo')
        arquivo.close()

with My_Open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WRITE', arquivo)