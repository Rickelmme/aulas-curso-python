import json

# pessoa = {
#     'nome': 'Rickelmme',
#     'sobrenome': 'Barreto',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.70,
#     'numeros_preferidos': (4, 7, 9),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#         )

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])