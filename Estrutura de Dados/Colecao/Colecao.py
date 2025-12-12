## Set é uma estrutura de coleção, que não armazena valores repetidos

numeros = set([1,2,3,1,3,4])

fruta = set("abacaxi")

carros = set(("palio","gol","celta","palio"))

print(numeros)
print(fruta)
print(carros)

linguagens = {"python", "java", "python", "c"}
print(linguagens)

nums = {1,2,3,2}

nums = list(nums)

print(nums[1])

for index, carro in enumerate(carros):
    print(f'{index}: {carro}')