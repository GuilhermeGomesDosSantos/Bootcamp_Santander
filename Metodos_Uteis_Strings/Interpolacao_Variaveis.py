nome = "Guilherme"
idade = 22
profissao = "Programador"
linguagem = "Java"

dados = {"nome": "Guilherme", "idade": 22}

saldo = 45.2543

print("Nome: %s idade: %d" %(nome,idade))
print("Nome: {} idade: {}".format(nome, idade))
print("Nome: {name} idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo:{saldo:.2f}")