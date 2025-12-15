def calculadora(numeros):
    return sum(numeros)


def retorno_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

##    return f"Antecessor: {antecessor} e Sucessor: {sucessor}"
    return antecessor, sucessor

def ola_mundo():
    print("Hello World!")
    return None

print(retorno_antecessor_e_sucessor(4))

print(calculadora([1, 3, 5, 7, 9]))

print(ola_mundo())

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

print(salvar_carro("Fiat", "Palio", "1992", "ABC-1234"))
print(salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234"))
salvar_carro(**{"marca":"Fiat", "modelo":"Palio","ano":1994,"placa":1212-3333})