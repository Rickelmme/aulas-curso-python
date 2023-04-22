# Atributos de classe
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Rick', 18)
p2 = Pessoa('Gabi', 16)
print(p1.get_ano_de_nascimento())
print(p2.get_ano_de_nascimento())