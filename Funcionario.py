#classe funcionario

#importando a classe pessoa
from Pessoa import Pessoa
class Funcionario(Pessoa):
    #metodo construtor da classe filha
    def __init__(matricula):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor

#override metodo str

    def __str__(self):
        return f'{super().__str__()}, Matricula: {self.matricula}, Salario: {self.salario}, Setor: {self.setor}'
