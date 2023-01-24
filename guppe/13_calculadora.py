print()
print('Seja Bem vindo a calculadora Python.')
print('RENAN ENTERPRISES SA, ALL RIGHTS RESERVED')

print()

print('Aqui você será capaz de realizar operações de *, /, + e -.')
print('EM BREVE MAIS FUNCIONALIDADES, ACALMEM-SE.')

print('Gostaria de começar? ')
print('Digite S para sim, e N para não: ')

comecar = input()
comecarmaiusculo = comecar.upper()

if comecarmaiusculo == 'S':
    print('Vamos lá!!!')
    print()
    num1 = float(input('Escolha o primeiro número: '))
    operacao = input('Qual a operação desejada: (+, -, *, /)')
    num2 = float(input('Escolha o segundo número: '))
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '/':
        resultado = num1 / num2
    elif operacao == '*':
        resultado = num1 * num2
    print()
    print(f'O resultado é {resultado}')
else:
    print('Então tá, até a próxima!!!')

