nome = 'Rickelmme Barreto'
altura = 1.70
peso = 60
imc = peso / altura ** 2

"f strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é: '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Rickelmme Barreto tem 1.70 de altura,
# pesa 60 quilos e seu IMC é 
# 20.761245674740486