## a Tupla é irmã da lista, é muito parecido com a lista
## a principal diferença é que tuplas são IMUTÁVEIS enquanto listas são MUTÁVEIS.
## podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgulas de parentes "()"
# tuplas pode armazenar outras tuplas


frutas = ("laranja", "pera", "uva","pera",)

letras = tuple("python")

numeros = tuple([1,2,3,4]) ## convertendo uma lista em tupla

pais = ("Brasil",)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

tup = ("1","3","5","7","9",)

tupla = ("p","y","t","h","o","n",)

print(frutas)
print(letras)
print(numeros)
print(pais)
print(frutas[-1])
print(frutas[2])
print(numeros[-2])
print(numeros[1])
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# tup[0] = 10
# print(tup)

carros = ("gol", "celta", "palio","BMW", "Ferrari", "Mercedes")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

linguagens = ("COBOL", "Ruby", "Java", "Python", "JS","C", "C++")

print(linguagens.count("COBOL")) ## count conta quantas vezes esse valor aparece na tupla
print(linguagens.count("Java"))
print(len(linguagens))
print(linguagens.index("Python")) ## index retorna a posição desse valor