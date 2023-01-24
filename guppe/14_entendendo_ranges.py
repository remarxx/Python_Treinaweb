"""
Ranges

Precisamos conhecer o loop for para usar os ranges.
Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, nao aleatórias.
Porém maneiras especificadas.

Formas gerais:

- Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

Exemplo:

for num in range(11):
    print(num)

- Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

Exemplo:

for num in range(4, 11):
    print(num)

Forma 3:

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

Exemplo:

for num in range(4, 11, 2):
    print(num)

Forma 4 (inverso):

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

Exemplo:

for num in range(10, -1, -1):
    print(num)
"""

for n in range(100000000000, -1, -5000):
    print(n)

