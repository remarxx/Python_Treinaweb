t = int(input())
nomes_list = list()

for i in range(t):
    nome = input()
    nomes_list.append(nome)

for i in range(t):
    print(f'{nomes_list[i]}', end=' ')

