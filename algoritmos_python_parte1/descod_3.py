"""
Dado uma lista de produtos com as informações: Id, Nome e Quantidade. Ordene os dados de forma que sejam listados de
acordo com os produtos com mais quantidade, os seja, a quantidade em ordem decrescente. Caso dois produtos tenham a
mesma quantidade, eles devem ser exibidos em ordem alfabética. Caso dois produtos tenham o mesmo nome, eles devem ser
listados pelo id em ordem crescente.
Entrada de dados
5
33 Monitor 10
85 Mouse 7
56 Notebook 3
19 Processador 23
22 HD 7
"""

class Produto:
    def __init__(self, id, nome, quantidade):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

if __name__ == '__main__':

    t = int(input())
    produtos = list()
    for i in range(t):
        id, nome, quantidade = input().split(' ')

        produto = Produto(int(id), nome, int(quantidade))
        produtos.append(produto)

    for x in range(len(produtos)):
        index_menor = x
        for j in range(int(x + 1), len(produtos)):
            if produtos.[j] < numeros[index_menor]:
                index_menor = j


        temp = numeros[index_menor]
        numeros[index_menor] = numeros[i]
        numeros[i] = temp
        print(numeros)

    for p in produtos:
        print(p.nome)