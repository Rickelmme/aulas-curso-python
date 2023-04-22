  #     01234567891011
nome = 'Rick Barreto' # Iteráveis
 
add = 0
new = ''

while add < len(nome):
    
    cada_letra = nome[add]
    new += f'-{cada_letra}'
    add += 1

new += '-'
print(new)
