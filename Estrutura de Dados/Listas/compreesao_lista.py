numeros = [10, 23, 55, 12, 20, 4, 6, 99, 11, 8, 1]
pares = []
quadrado = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) ## append adiciona valores na lista
    
print(pares)

pares_lista_compreesao = [numero for numero in numeros if numero % 2 == 0]
print(pares_lista_compreesao)

for numeroQuadrado in numeros:
    if numeroQuadrado % 2 == 0:
        quadrado.append(numeroQuadrado ** 2)

print(quadrado)

quadrado_compreesao = [numero_Quadrado ** 2 for numero_Quadrado in numeros if numero_Quadrado % 2 == 0]

print(quadrado_compreesao)