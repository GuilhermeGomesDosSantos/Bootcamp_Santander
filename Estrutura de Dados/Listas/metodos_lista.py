lista_1 = []
lista_2 = ["Python", 2, 4, 6, 11]
lista_3 = ["vermelho", "azul", "verde"]
lista_4 = ["java", "python", "c","ruby", "java","python","COBOL"]
lista_5 = []


lista_1.append(1)
print(lista_1)

lista_1.append("Python")
print(lista_1)

lista_1.append([40, 10, 20])
print(lista_1)

lista_1.clear()
print(lista_1)

lista_2_copia = lista_2.copy()
print("Lista 2 ID:",id(lista_2), "Lista 2 Copia ID: ",id(lista_2_copia)) ## São objetos diferentes

print(lista_3.count("vermelho"))
print(lista_3.count("azul"))
print(lista_3.count("verde"))

lista_4.extend(["csharp", "go", "java"])
print(lista_4)

print(lista_4.index("python"))
print(lista_4.index("java"))

lista_4.pop()
print(lista_4)

lista_4.pop(5)
print(lista_4)

lista_4.remove("ruby")
print(lista_4)

## A diferença entre pop() e ruby(), é que pop remove passando o indice, já o remove remove passando o objeto

lista_4.reverse()
print(lista_4)

lista_4.sort()
print(lista_4)

lista_4.sort(reverse=True)
print(lista_4)

lista_4.sort(key=lambda x: len(x))
print(lista_4)

lista_4.sort(key=lambda x: len(x), reverse=True)
print(lista_4)

print(len(lista_4))

print(sorted(lista_4, key=lambda x: len(x)))
print(sorted(lista_4, key=lambda x: len(x), reverse=True))
print(sorted(lista_4))