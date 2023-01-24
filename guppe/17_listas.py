"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
DINÃMICAS e também de pordermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você quiser criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: [];


"""

lista = [1, 3, 10, 45, 6, 78, 9, 0]
lista.sort()
# print(lista)

listastr = ['R', 'e', 'n', 'a', 'n']

listarng = list(range(1, 30+1))

print(lista)
print(listastr)
print(listarng)

listanome = list('Renan Marques da Silva')
print(listanome)
listanome.sort()
listanome.reverse()

print(listanome)

if 'R' in listanome:
    print("Achei R")
else:
    print("lascou")