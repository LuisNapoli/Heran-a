#classe Aluno

#importando classe Professor
from Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, salario, setor, curso, semestre):
        super().__init__(nome,cpf,idade)
        self.curso =  curso
        self.matricula = matricula
        self.semestre = semestre

    def __str__(self):
        return f'{super().__init__}, Matricula: {self.matricula}, Curso: {self.curso}, Semestre: {self.semestre}'