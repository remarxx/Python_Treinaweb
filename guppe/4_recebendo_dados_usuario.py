import datetime
"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angeline Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''

"""

# - Aspas duplas triplas -> """Angelina Jolie"""


# Entrada de dados
# print('Qual seu nome?')
# nome = input()
# print()

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print moderno. 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual'
print(f'Seja bem vindo(a) {nome}')
print()

idade = int(input("Qual sua idade? "))

# print("Qual a sua idade?")
# idade = input()

# Processamento

# Saída
# Exemplo de print ántigo'2.x
# print('A %s tem %s anos' % (nome, idade))
# print('O %s tem %s anos' % (nome, idade))

# print('{0} tem {1} anos'.format(nome, idade))
hoje = datetime.date.today()

ano = hoje.year

print(f'{nome}, nasceu em {ano - idade} e tem aproximadamente {idade} anos')


# data = datetime.date(2025, 4, 16)

# print(data.ctime())
# ano = data.year

# print(ano)




