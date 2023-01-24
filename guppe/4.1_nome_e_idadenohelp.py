import datetime

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

print(f' O nome do usuário é {nome}')
print(f' A idade do usuário é {idade}')

hoje = datetime.date.today()
anocorrente = hoje.year

print(f' O usuário nasceu em {anocorrente - idade}')
