def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}")

##exibir_mensagem()
exibir_mensagem_2("GDS")
exibir_mensagem_2(nome="Gui")
exibir_mensagem_3()
exibir_mensagem_3(nome="Fulano")
exibir_mensagem_3("Teste")