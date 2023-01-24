"""
Tipo String.

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples = 'uma string', 'a', 'True'
- Estiver entre aspas duplas = "uma string"
- Estiver entre aspas simples triplas = '''uma string'''
"""
# Estiver entre aspas duplas triplas = """uma string"""

nome = 'Renan'
print(nome)
print(type(nome))

nome2 = "Marques"
print(nome2)
print(type(nome2))

nome3 = '''Da Silva'''
print(nome3)
print(type(nome3))

nome4 = """Bonitão"""
print(nome4)
print(type(nome4))

# Pular uma linha

nome5 = 'Angelina \nJolie'
print(nome5)

nome6 = """Angelina
Jolie"""
print(nome6)

print(nome.upper())
print(nome.lower())
print(nome3.split())  # transforma em  uma lista de strings

print(nome6[0:8])  # Se chama slice de string.

# Inversão da String

nomeparasplitar = 'Renan Marques'
print(nomeparasplitar[::-1])

# Substituir uma String na variável

print(nomeparasplitar.replace('R', 'L'))

textoparainverter = 'socorram me subino onibus em marrocos'  # Isso se chama palíndromo

print(textoparainverter)
print(textoparainverter[::-1])




