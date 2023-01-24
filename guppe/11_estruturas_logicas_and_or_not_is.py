"""
Estruturas Lógicas: and, or, not, is.

Operadores unários: not.
Operadores binários: and, or, it.

Para o and, ambos os valores precisam ser True.
Para o or, um ou outro valor precisa ser True.
Para o not, o valor do booleano é invertido, ou seja, se for True, vira Flase, se for False vira True.
Para o is, o valor é comparado a um segundo.
"""

ativo = True
logado = False

"""
if not ativo:
    print('Você precisa ativar sua conta. Por favor cheque seu email.')
else:
    print('Bem-vindo MOTHAFOCA')
"""

if ativo:
    print('SÓ OS BRABO')
else:
    print('DEU RUIM PAPAI É ISSO')

# teste = input()
# print(type(teste))

# Ativo é verdadeiro?
print(ativo is False)

