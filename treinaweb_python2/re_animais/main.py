import cachorro
import gato

espuminha = cachorro.Cachorro('Shih Tzu', 4, False, 100)

print(f'O tipo desse objeto é: {espuminha.tipos}')
# print(f'A quantidade de patas desse objeto é: {espuminha.qtde_patas}')
# print(f'Esse objeto pode ser considerado selvagem?: {espuminha.is_salvage}')
# print(f'O quanto de energia ele parece ter no momento? Está bem alimentado? {espuminha.qtde_energia}')

print(f'Forçando, o novo tipo do objeto é: {espuminha.tipos}')
fred = gato.Gato('Persa', 4, False, 70)

fred.__is_salvage = True
print(f'O animal é {fred.__is_salvage}')
fred._qtde_energia = 2
fred.__qtde_patas = 19

# if not fred.is_salvage:
#    print(f'A raça do objeto é {fred.tipo}, ele tem {fred.qtde_patas} patas, é um animal dócil e está com '
#          f'{fred.qtde_energia}% de energia')
# else:
#     print(f'A raça do objeto é {fred.tipo}, ele tem {fred.qtde_patas} patas, é um animal selvagem e está com '
#          f'{fred.qtde_energia}% de energia')

fred.andar_passos(5)
# print(fred.qtde_passos)

fred.andar_passos(5)
# print(fred.qtde_passos)

fred.andar_passos(10)
fred.andar_passos(10)
# print(fred.qtde_passos)

fred.pular(10)
# print(fred.altura_pulo)

fred.comer(30)
# print(fred.qtde_energia)

espuminha.acordar()
# print(espuminha.animal_awake)

espuminha.acordar()

print(espuminha.tipos)
espuminha.__tipo = 'Zoologico'
print(espuminha.tipos)



