## Operadores de identidade comparam se duas variáveis se referem ao mesmo objeto na memória, usando is e is not

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)