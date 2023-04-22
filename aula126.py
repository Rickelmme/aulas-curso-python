# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Rick', 'idade': 18}
p1 = Pessoa(**dados)
print(vars(p1))
print(p1.nome)