"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java:

For(int i = 0; i < 10; i++){
    // execução do loop.
}

Python

for item in interavel:
    // execução do loop

    Utilizamos loops para iterar sobre sequencias ou sobre valores interaveis.
    Exemplos de iteráveis:

    - String
        nome = 'Geek University'
    - Lista
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)

# Exemplo de for 1: (Iterando em uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2: (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3: (Iterando em uma range)

range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)
"""

nome = 'Geek University'
lista = [1, 3, 5, 6, 9, 10, 20]
numeros = range(1, 10)  # Temos que transformar em uma lista.

"""
Enumerate:

 ((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...)
 

for indice, letra in enumerate(nome):
    print(nome[indice])
print()

for indice, letra in enumerate(nome):
    print(letra)
print()

for _, letra in enumerate(nome):  # Quando não precisamos de um valor, podemos utilizar _ para descartá-lo.
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo número {n}')

print()
print('Vamos somar um número ao outro?')
qtd = int(input('Quantas vezes esse loop deve rodar, para realizar as somas? '))

result = 0

for n in range(1, qtd+1):
    soma = int(input(f'Informe o número {n}/{qtd}: '))
    result = soma + result

print(f'O resultado da soma é: {result}')

"""

"""

print()
print('Vamos somar um número ao outro!?')
print()
print("Quantas vezes esse loop deve rodar, para realizar as somas?")
qtde = (input('Digite: '))

qtdpararange = int(qtde)
print(f'O usuário quer repetir o programa por {qtdpararange} vezes.')

soma = 0

for n in range(1, qtdpararange+1):
    num = int(input('Digite um número para a soma: '))
    soma = num + soma

print(f'A soma resulta em {soma}', end='')

"""

for _ in range(7):
    for num in range(1, 11):
        print('A' * num)

print('67' * 5)