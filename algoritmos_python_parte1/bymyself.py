numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(tamanho):
    # 0 .. 5
    valor = int(input(f"Digite o número do vetor na posição {i}: "))
    numeros.append(valor)
print("Vetor: ", numeros)

# BUSCA LINEAR

numeros_pesquisar = int(input('Qual número gostaria de pesquisar? '))
posicao_resultado = -1

for i in range(tamanho):
    if numeros[i] == numeros_pesquisar:
        posicao_resultado = i
        break

if posicao_resultado < 0:
    print(f'O número {numeros_pesquisar} não foi encontrado.')
else:
    print(f'O número {numeros_pesquisar} está na posição {posicao_resultado}')

# FIM BUSCA LINEAR

print(numeros)

for i in range(tamanho):
    posicao_menor = i  # 5
    for j in range(int(i + 1), tamanho):
        if numeros[j] < numeros[posicao_menor]:
            posicao_menor = j
        temp = numeros[posicao_menor]