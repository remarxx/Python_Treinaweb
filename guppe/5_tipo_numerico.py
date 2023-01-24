"""
Tipo numérico
"""
print('Divisão normal.')
print(5/2)
print()

print('Divisão inteira.')
print(int(5/2))
print()

print('Ou...')
print(5//2)
print()

print('Qual é o resto?')
print(5%2)
print(4%2)
print('Uma boa maneira de descobrir se o número é par ou ímpar.')
print()

print('Potenciação.')
print(5**2)
print()

# Command + L = limpa tela.

print('Ao falar de números grandes...')
num = int(1_000_000_000_000_000_000_000_000)
print(f'Podemos utilizar números assim: {num}')
print()

print('Soma do número a direita, ou item recebe item mais o número da direita...')
numerosoma = 10
print(numerosoma + 2)
print('Ou...')
numerosoma += 2
print(numerosoma)
print()

print('Multiplica o número a direita, ou item recebe item vezes o número da direita...')
numeromultiplicacao = 10
print(numeromultiplicacao * 2)
print('Ou...')
numeromultiplicacao *= 2
print(numeromultiplicacao)
print()

print('Divide o número a direita, ou item recebe item e divide pelo número da direita...')
numerodivisao = 10
print(numerodivisao / 2)
print('Ou...')
numerodivisao /= 2
print(numerodivisao)
print()

print(type(numeromultiplicacao))
