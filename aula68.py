# x = 1

# def escopo():
#     x = 10


#     def outra_funcao():
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x)

x = 0

def escopo_1():
    x = 1

    def escopo_2():
        x = 2
        print(x)
        
    escopo_2()
    print(x)

escopo_1()
print(x)