# Arquivo Principal
from Pessoa import Pessoa
from Funcionario import Funcionario

#objeto da classe pessoa
p1 = Pessoa('Joao','123',20)

#Imprimir dados do objeto
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())


#objeto funcionario
f1 = Funcionario('Jose','456',40,'0099', 2526.45, 'biblioteca')
#objeto aluno
f2 = Aluno('Carlos','24',"Arquitetura")
# objeto em versão texto

print(f1.get_nome())
print(f1)
print(f2)