def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da opração é = {resultado}")

opration = somar

exibir_resultado(10, 10, somar)
exibir_resultado(30, 20, subtrair)
print(opration(20,10))