# Introdução ás Generator fuctions em Python
# generator = (n for n in range(100))

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1
        
        if n > maximun:
            return
        
    # yield 1  # pausado
    # print('Continuando...')
    # yield 2 # pausado
    # print('SOU BOM')
    # yield 3 
    # print('Vou terminar')
    # return 'ACABOU'

gen = generator(maximun=10)
for n in gen:
    print(n)
