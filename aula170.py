# os.listdir para navegar em caminhos
# \Users\Positivo\Desktop\curso_python
import os

caminho = os.path.join('/Users', 'Positivo', 'Documents', 'Praticando Python')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for documentos in os.listdir(caminho_completo_pasta):
        print(' ', documentos)
