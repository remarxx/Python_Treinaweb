"""

class PrimeiraClasse:
    def __init__(self, curso, descricao):
        self.curso = curso
        self.descricao = descricao
        


t = int(input())

for i in range(0, t):
    a, b, n = input().split()

    inta = int(a)
    intb = int(b)
    intn = int(n)

    lista = inta, intb, intn

    for x in range(0, intn):

        pot = pow(2, 0)

        lista = inta + pot + intb
        for y in lista:
            print(lista[y])

        print(type(lista))

        pot = pow(2, 0)

        lista.append(pot)

        # for y in lista:
        # print(lista[y])

---

t = int(input())

for i in range(0, t):
    a, b, n = input().split()

    inta = int(a)
    intb = int(b)
    intn = int(n)
    result1 = inta

    for z in range(0, intn):
        potenciacao = pow(2, z)
        # print(type(potenciacao))

        result1 = (potenciacao * intb) + result1
        print(result1, end=' ')

        # print(type(result1))

        # result2 = (inta + potenciacao * intb + 2 * intb)
        # print(result2)
        # print(type(inta))

"""
import re

"""
n = int(input())
lista = []

for i in range(0, n):

    try:
        a, b = input().split()
        aa = int(a)
        bb = int(b)
        result = aa // bb
        print(result)

    except ZeroDivisionError as e:
        print(f'Erro: {e}')
    except ValueError as f:
        print(f'Erro: {f}')


# Coloque o seu código aqui

"""

n = int(input())

for i in range(0, n):


