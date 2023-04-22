# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas.')

texto = 'Python'
novo_texto = ''
for letras in texto:
    novo_texto += (f'*{letras}')
    print(letras)
print(novo_texto + '*')
