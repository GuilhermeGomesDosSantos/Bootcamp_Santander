saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)

print(saque <= limite)

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

print(not 1000 > 1500) ## vai retornar o inverso do booleano

contatos_emergencia = []

print(not contatos_emergencia)

print(not "saque 1500;")

print(not "")

conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))