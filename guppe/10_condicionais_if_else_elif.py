"""
Estruturas condicionais if, else e elif

# Estrutura condicional em C:

if(idade < 18){
    printf("Menor de idade");
}else if{idade == 18){
    print("Tem exatamente 18 anos");
}else{
    print("É menor de idade");
}

# Estrutura condicional em Java:

if(idade < 18){
    System.out.println("Menor de idade");
}else if{idade == 18){
    System.out.println("Tem exatamente 18 anos");
}else{
    System.out.println("É menor de idade");
}


"""

idade = int(input('Digite sua idade: '))
status = True

if status == True:
    if idade < 18:
        print("Menor de idade")
    elif idade == 18:
        print('Tem exatamente 18 anos')
    elif idade is 0:
        print('Pelo jeito nem nasceu.')
    else:
        print('É maior de idade')
else:
    print('Inicie o programa.')
