from usuario import Usuario

"""
usuario1 = Usuario('Renan', 'Marques', 31)
print('Olá, {} {}, você tem {} anos de idade.'.format(usuario1.nome, usuario1.sobrenome, usuario1.idade))



objeto_usuario1 = Usuario('Renan', 'Marques', 31)

for x in range(1, 10):
    print(f'Olá, {objeto_usuario1.nome} {objeto_usuario1.sobrenome}, sua idade é {objeto_usuario1.idade}')
    if x == 2:
        print('O loop entrou no 2 e reiniciou')
        continue
    if x == 8:
        print('O loop entrou no 8')
        break

    print(x)
    if objeto_usuario1.idade >= 18:
        print(f'{objeto_usuario1.nome} é maior de idade')
    else:
        print(f'{objeto_usuario1.nome} é menor de idade')
else:
    print("O loop entrou no else.")
    
"""

continuar = 1

lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        idade = int(input('Digite sua idade: '))
        objeto_usuario = Usuario(nome, sobrenome, idade)

        lista_usuarios.append(objeto_usuario)

        if idade == 99:
            break

        if idade == 98:
            continue

        print(f'Olá, {objeto_usuario.nome.title()} {objeto_usuario.sobrenome.title()} sua idade é {objeto_usuario.idade}')

    #    media_idades = objeto_usuario1.idade + objeto_usuario2.idade / 2
    #    print(f'A média das idades é {media_idades}')

        if objeto_usuario.idade <= 14:
            print('{} é crianca'.format(objeto_usuario.nome.title()))
        elif 15 <= objeto_usuario.idade <= 17:
            print(f'{objeto_usuario.nome.title()} é adolescente')
        elif 18 <= objeto_usuario.idade <= 50:
            print('{} é adulto'.format(objeto_usuario.nome.title()))
        else:
            print(f'{objeto_usuario.nome.title()} é idoso')

        print('Deseja continuar cadastrando?')
        continuar = int(input('Digite 1 para SIM, e 0 para NÃO: '))
    except ValueError:
        print('Digite um número válido.')
else:
    print('Você encerrou o programa. Segue lista de usuários cadastrados: ')

    for x in lista_usuarios:
        print(f'Usuário {lista_usuarios.index(x)} - Nome completo: {x.nome.title()} {x.sobrenome.title()}, com idade de: {x.idade}')
