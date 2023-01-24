"""
Escopo de variáveis.

/                              /

Escopo é um lugar delimitado.

1 - Variáveis globais.
    - Variáveis gobais são redconhcidas, ou seja, seu escopo compreende, TODO O PROGRAMA.

2 - Variáveis locais.
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escolpo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma varíavel, nós não colocamos o
tipo de variável dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C ou Java:

int numero = 42;

"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 10
print(numero)

if numero > 2:
    novo = numero + 445  # Exemplo de variável local, só existe se a condição também for aceita. Está dentro do if.
    print(novo)

print(novo)

