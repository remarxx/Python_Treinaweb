"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais no python é ponto e não vírgula.

"""

# Errado
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível
valor1, valor2 = 1, 55
print(valor1, valor2)
print(type(valor1))
print(type(valor2))

# Convertendo um número float para int

numquebrado = 23.5667
numquebradotointer = int(numquebrado)
print(numquebradotointer)
print(type(numquebradotointer))

# Numero complexo... Adicione o j.

complexo = 5j
print(type(complexo))

