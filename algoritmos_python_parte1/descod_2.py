t = int(input())
nomes_list = list()

for i in range(t):
    nome = input()
    nomes_list.append(nome)

nome_pesquisa = input()
posicao_resultado = -1

for i in range(t):
    if nomes_list[i] == nome_pesquisa:
        posicao_resultado = i
        break

if posicao_resultado == -1:
    print(-1)
else:
    print(posicao_resultado)



