"""
Loop While

Forma geral

while expressao_booleana:
    //execucao do loop

O Bloco do while será repetido enquanto a expressão booleana for verdadeira.


print('Bem vindo')
print('Digite um número, e se ele for maior que 5, resultará em POSITIVO.')
print('Caso for menor, resultará em NEGATIVO, e o programa se encerrará.')


num = int(input('Digite um número: '))

while num > 5:
    print('Deu certo.')
    num = int(input('Digite um número: '))
print('Negativo')

num = 0

while num <= 10:
    print(num)
    num = num + 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

"""

resposta = " "

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
