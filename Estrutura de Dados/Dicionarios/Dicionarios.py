pessoa_1 = {"nome": "Guilherme", "idade": 22}
print(pessoa_1)

pessoa_2 = dict(nome = "Guilherme", idade = 22)
print(pessoa_2)

pessoa_2["telefone"] = "3333-1234"
print(pessoa_2)

print(pessoa_2["nome"])
print(pessoa_2["idade"])
print(pessoa_2["telefone"])

contatos = {
    "guiteste1@teste.com": {"nome": "Guilherme", "idade": 22, "telefone":"1111-2222"},
    "joseteste1@teste.com": {"nome": "José", "idade": 64, "telefone":"6666-3333", "extra":{1,2,3,4,5,6,7}}
}
print(contatos)

print(contatos["joseteste1@teste.com"]["extra"])

for chave, valor in contatos.items():
    print(chave, valor)

for chave in contatos:
    print(chave, contatos[chave])