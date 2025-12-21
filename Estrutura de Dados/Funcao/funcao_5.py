salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista_aux = {lista_aux}")
    salario += bonus
    return salario


lista = [1]
print(salario_bonus(1000, lista))
print(lista)