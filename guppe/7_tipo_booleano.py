"""
TIpo Boolano

Álgebra Booleana, criada por George Boole,

2 constantes, Verdadeiro ou Falso.

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado: true, false
Certo: True, False

"""

ativo = True
print(ativo)


"""
Operações Básicas:
"""

# NEGAÇAO (not)

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for
falso o resultado será verdadeiro. Ous seja, sempre o contrário.
"""

print(f'A princípio, a varíavel booleana tem o valor: {ativo}')
print(f'Porém, ao realizar a negação, o valor fica: {not ativo} ')

# Ou (or)

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True = True
True or False = True
False or True = True
False or False = False
"""

# E (and)

"""
É uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiras.

True and True = True
True and False = False
False and True = False
False and False = False
"""






