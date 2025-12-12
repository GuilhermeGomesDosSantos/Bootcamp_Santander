conjunto_a = {1,2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_c = {10, 20, 30,55}
conjunto_d = {10, 40, 70, 55}

print(conjunto_c.intersection(conjunto_d))

conjunto_e = {1,2,3,4}
conjunto_f = {2,3,4,5}

print(conjunto_e.difference(conjunto_f))
print(conjunto_f.difference(conjunto_e))

print(conjunto_e.symmetric_difference(conjunto_f))

conjunto_g = {1,2,3}
conjunto_h = {4,1,2,5,6,3}

print(conjunto_g.issuperset(conjunto_h))
print(conjunto_h.issuperset(conjunto_g))

conjunto_i = {1,2,3,4,5}
conjunto_j = {6,7,8,9}
conjunto_k = {1,0}

print(conjunto_i.isdisjoint(conjunto_j))
print(conjunto_i.isdisjoint(conjunto_k))

sorteio = {1, 22, 44}
sorteio.add(1)
print(sorteio)
sorteio.add(34)
print(sorteio)

sorteio.clear()
print(sorteio)

sorteio.add(1)
sorteio.add(55)
print(sorteio)

sorteio.copy()

numeros = {1,2,5,2,1,6,8,9,4}
numeros.discard(2)

print(numeros)

numeros.pop()
print(numeros)

numeros.remove(4)
print(numeros)

print(len(numeros))

print(1 in numeros)
print(8 in numeros)