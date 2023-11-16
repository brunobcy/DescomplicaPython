Nome       = input("Digite o seu nome:")
Nascimento = input("Qual seu ano de nascimento:")
Email      = input("Digite seu E-amil:")
CPF        = input("Digite o seu CPF: ")
RG         = input("Digite o seu RG: ")
Cod_Matricula = input("Digite o seu Cod de Matricula: ")


print("Nome:", Nome, ". E-mail:",Email , ". Nascimento:",Nascimento,". CPF",CPF )

print("Nascimento")
print(Nascimento)
print("E-mail:")
print(Email)

a = int(input("Digite um numero: "))
print(a+5)
a = 2
b = 3

print(a**b)


 
from math import sqrt


print(sqrt(4))

idade = int(input("Digite a sua Idade: "))

if idade > 18:
    print("È maior de Idade")
elif idade == 18:
    print("È Guerreiro Jedi")
else:
    print("É MENOR de Idade")

idade = int(input("Digite sua Idade:"))
print ("É Maior") if idade >= 18 else print ("È MENOR")


a = "MARCIO"
match a: 
    case "antinio":
        print("não e MARCIO")
    case "Marcio":
        print("ACHOU MARCIO")

anoNascimento = int(input("Digite o seu ano de Nascimento:"))
anoAtual      = int(input("Digite o ano atual:"))
Idade = anoAtual - anoNascimento

if Idade >= 18:
    print("Digite o titulo")
else:
    print("Digite Documento de Responsável")

for a in range(5):
    print("Marcio")

a = ["Marcio", "Bruno", "Fernado","haroldo","Larissa"]

for a in a:
    print(a)

a = []
b = 1
print(a)

while b<= 3:
    a.append(input("Digite um nome de Aluno: "))
    b = b + 1
print(a)

a=["Marcio","Bruno"]
a.insert(1,"Hellen")
print(a)
a.remove("Marcio")
print(a)
