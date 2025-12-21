def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234",marca="Fiat", motor="1.0",combustivel="Gasolina") ## valido

##criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") ## inválido

def criar_carro_1(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, motor, combustivel)

criar_carro_1(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="Fiat", combustivel="1.0")

def criar_carro_2(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
