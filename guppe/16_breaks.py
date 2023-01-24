"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

"""

for numero in range(1, 111):
    if numero == 103:
        break
    else:
        print(f'O número é {numero}')
print('Chegamos ao 102????')

# Exemplo 2

while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break
print('Você encerrou o programa.')
