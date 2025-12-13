contatos = {
    "guiteste1@teste.com": {"nome": "Guilherme", "idade": 22, "telefone":"1111-2222"},
    "joseteste1@teste.com": {"nome": "José", "idade": 64, "telefone":"6666-3333"}
}

print(contatos)

# contatos.clear()
copia = contatos.copy()
copia["guiteste1@teste.com"] = {"nome":"Gui"}
print(contatos["guiteste1@teste.com"])
print(copia["guiteste1@teste.com"])

teste_1 = dict.fromkeys(["nome", "telefone"])
teste_2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(teste_1)
print(teste_2)

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guiteste1@teste.com"))

print(contatos.keys())

resultado_1 = contatos.pop("guiteste1@teste.com")
resultado_2 = contatos.pop("guiteste2@teste.com", "não encontrado")
print(contatos)
print(resultado_1)
print(resultado_2)

contatos_2 = {
    "guiteste1@teste.com": {"nome": "Guilherme", "idade": 22, "telefone":"1111-2222"},
    "joseteste1@teste.com": {"nome": "José", "idade": 64, "telefone":"6666-3333"}
}

print(contatos_2)
contatos_2.popitem()
print(contatos_2)

contato_3 = {"nome": "Guilherme", "telefone": "3333-2222"}
contato_3.setdefault("nome", "Giovanna")
print(contato_3)

contato_3.setdefault("idade", 22)
print(contato_3)

contato_4 = {
    "guilhermeteste@gmail.com": {"nome":"Guilherme", "idade":22, "telefone":"3333-2222"}
}
contato_4.update({"guilhermeteste@gmail.com": {"nome":"GDS"}})
print(contato_4)

contato_4.update({"fulano@gmail.com":{"nome":"Fulano Teste", "idade": 44, "telefone":"1212-4534"}})
print(contato_4)

print(contato_4.values())

contatos_5 = {
    "guiteste1@teste.com": {"nome": "Guilherme", "idade": 22, "telefone": "1111-2222"},
    "joseteste1@teste.com": {"nome": "José", "idade": 64, "telefone": "6666-3333"},
    "mariateste1@teste.com": {"nome": "Maria", "idade": 31, "telefone": "9999-8888"},
    "carlosteste1@teste.com": {"nome": "Carlos", "idade": 45, "telefone": "7777-1212"},
    "anatest01@teste.com": {"nome": "Ana", "idade": 27, "telefone": "5555-2323"},
    "paulotest02@teste.com": {"nome": "Paulo", "idade": 52, "telefone": "4444-4545"}
}

print("guiteste1@teste.com" in contatos_5)
print("emailteste@gmail.com" in contatos_5)
print("endereco" in contatos_5["guiteste1@teste.com"])
print("telefone" in contatos_5["guiteste1@teste.com"])

del contatos_5["guiteste1@teste.com"]["nome"]
del contatos_5["anatest01@teste.com"]
print("Deletados", contatos_5)