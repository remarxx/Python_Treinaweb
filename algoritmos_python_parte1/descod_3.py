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

# Capturar objetos no list()

        for m in produtos:
            for o in range(0, t):
                index_maiorqtde = m
                for j in range(o + 1, t):
                    if m.quantidade > quantidade[index_maiorqtde]:
                        index_maiorqtde = j
                temp = produtos[index_maiorqtde]
                produtos[index_maiorqtde] = produtos[m]
                produtos[m] = temp
                print(m.id, m.nome, m.quantidade)

""" Informe seu código aqui

print()

for p in produtos:
    print(p.nome)
    
        for obj in produtos:
            print(obj.id, obj.nome, obj.quantidade, sep=' ')
        print('') """