# os.walk
# os.walk é uma função que permite percorrer uma estrúturas de diretótios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'Positivo', 'OneDrive', 'Documentos')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', the_counter, 'FILES', caminho_completo_arquivo)
