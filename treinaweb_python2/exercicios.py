"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



if __name__ == "__main__":
   #p = Pessoa()

    Pessoa.nome = input()
    Pessoa.idade = input()

    print(f"Nome: {Pessoa.nome} - Idade: {Pessoa.idade}")



------------


class PrimeiraClasse():
    def __init__(self, a=0):
        self.a = a

    def ola(self):
        print('Bem-vindo a orientação a objetos')


if __name__ == "__main__":
    pc = PrimeiraClasse()

    pc.ola();

------------------

class Curso():
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

--------------


class MinhaClasse:
    def __del__(self):
        print('Finalizando execução')

if __name__ == "__main__":
    c = MinhaClasse()
    del c

--------------------------------------------------------------------------------------------------

# Desafio de código 4.1 (Herança)

class Aritmetica:
    def subtracao(self, num1, num2):
        a = num1 - num2
        return a


class Sub(Aritmetica):
    pass


if __name__ == "__main__":
    s = Sub()

    # Exibe o nome da superclasse
    print("Minha superclasse é: " + str(s.__class__.__bases__[0]))

    t = int(input())

    for i in range(0, t):
        var1, var2 = input().split()
        print(s.subtracao(int(var1), int(var2)))

--------------------------------------------------------------------------------------------------



class Animal:

    def andar(self):
        a = "Estou andando!"
        return print(a)

class Aquatico:

    def nadar(self):
        return print("Estou nadando!")

class Reptil(Animal, Aquatico):
    pass


if __name__ == "__main__":
    r = Reptil()

    # Exibe o nome das superclasses
    print("Minhas superclasses são: " + str(sorted(r.__class__.__bases__, key=lambda x: x.__name__)))

    r.andar()
    r.nadar()

--------------------------------------------------------------------------------------------------



import re
import inspect


# Informe seu código aqui.

class Carro:

    def __init__(self):
        self.__nome = None
        self.__tipo = None

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
if __name__ == "__main__":
    c = Carro()

    elementos = dict(vars(Carro))

    ## Membros da classe
    filtro = filter(lambda e: False if re.search(r'\b__\w+__\b', e) else True, dir(c))
    for membro in filtro:
        print(membro)
        if (membro in elementos):
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fget']))
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fset']))

    c.nome = input()
    c.tipo = input()

    print(c.nome)
    print(c.tipo)

--------------------------------------------------------------------------------------------------


import re
import inspect


class Carro:
    def __init__(self, tipo):
        self.__nome = None
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == "__main__":
    nome = input()
    tipo = input()

    c = Carro(tipo)
    c.nome = nome

    elementos = dict(vars(Carro))

    ## Membros da classe
    filtro = filter(lambda e: False if re.search(r'\b__\w+__\b', e) else True, dir(c))
    for membro in filtro:
        print(membro)
        if (membro in elementos):
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fget']))
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fset']))

    print(c.nome)
    print(c.tipo)
    
    -------------------------------------------------------------------------------------------------



import re
import insp


class Carro:
    def __init__(self):
        self._tipo = None
        self._nome = None

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

      @nome.setter
        def nome(self, nome):
            self._nome = nome

        @tipo.setter
        def tipo(self, tipo):
            self._tipo = tipo


if __name__ == "__main__":
    c = Carro()

    elementos = dict(vars(Carro))

    ## Membros da classe
    filtro = filter(lambda e: False if re.search(r'\b__\w+__\b', e) else True, dir(c))
    for membro in filtro:
        print(membro)
        if (membro in elementos):
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fget']))
            print(inspect.isfunction(dict(inspect.getmembers(vars(Carro)[membro]))['fset']))

    c._nome = input()
    c._tipo = input()

    print(c._nome)
    print(c._tipo)


import inspect


class Veiculo():
    def __init__(self):
        self.__nome = None
        self.__tipo = None

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def show_tipo(self):
        print(self.__tipo)


# Informe seu código aqui
class Moto(Veiculo):
    def show_tipo(self):
        print("Classe do tipo Moto")

if __name__ == "__main__":
    [print(i) for i in
     list(map(lambda x: x[1].__qualname__, inspect.getmembers(Moto, lambda m: inspect.isfunction(m))))]

    [print(i) for i in
     list(map(lambda x: x[1].__qualname__, inspect.getmembers(Moto.__base__, lambda m: inspect.isfunction(m))))]

    m = Moto()

    m.show_tipo()



import inspect


class Veiculo():
    def __init__(self, tipo):
        self.__nome = None
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def show_tipo(self):
        print(self.__tipo)


# Informe seu código aqui
class Carro(Veiculo):
    def __init__(self):
        super().__init__('Classe do tipo Carro')


if __name__ == "__main__":
    [print(i) for i in
     list(map(lambda x: x[1].__qualname__, inspect.getmembers(Carro, lambda m: inspect.isfunction(m))))]

    [print(i) for i in
     list(map(lambda x: x[1].__qualname__, inspect.getmembers(Carro.__base__, lambda m: inspect.isfunction(m))))]

    c = Carro()

    print(c.tipo)



# Dada uma classe Veiculo, defina uma classe Carro e implemente os métodos abstratos dela.
# Entrada de dados
# Corsa
# Sedan

import inspect
import abc


class Veiculo(abc.ABC):
    def __init__(self):
        self.__nome = None
        self.__tipo = None

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    @abc.abstractmethod
    def nome(self, nome):
        pass

    @tipo.setter
    @abc.abstractmethod
    def tipo(self, tipo):
        pass


# Informe seu

class Carro(Veiculo):
    def nome(self, nome):
        pass

    def tipo(self, tipo):
        pass


if __name__ == "__main__":
    [print(i) for i in
     list(map(lambda x: x[1].__qualname__, inspect.getmembers(Carro, lambda m: inspect.isfunction(m))))]

    c = Carro()

    c.nome = input()
    c.tipo = input()

    print(c.nome)
    print(c.tipo)



# Dado uma pseudo-interface InterfaceAritmetica, que define o método divisao_soma, defina uma classe chamada
# Calculadora que implementa esta classe e retorna a soma dos divisores de um valor.
# Por exemplo, os divisores do valor 6 é 1, 2, 3 e 6, a soma desses valores é 12.
# Entrada de dados
# 6
# Saída esperada
# Implementei: InterfaceAritmetica
# 12

import abc


class InterfaceAritmetica(abc.ABC):

    @abc.abstractmethod
    def divisao_soma(self, n):
        pass


# Informe seu código aqui
class Calculadora(InterfaceAritmetica):

#   def __init__(self, a=0):
#        self.a = a

#    def divisao_soma(self, b):
#        print(b*2)

    def divisao_soma(self, n):
        soma = 0

        for i in range(1, n + 1):
            if (n % i == 0):
                soma += i

        return soma

if __name__ == "__main__":
    c = Calculadora()

    print("Implementei: ", Calculadora.__base__.__name__)

    n = int(input())
    print(c.divisao_soma(n))



 Dado uma pseudo-interface InterfaceVeiculo, que declara o método show_tipo, defina duas classes, uma chamada
"Carro", que implementa o método da pseudo-interface e exibi a mensagem "Carro", e outra chamada Moto, que 
implementa o método da interface e exibe a mensagem "Moto".
Entrada de dados
Não há nenhuma entrada
Saída esperada
Carro
Moto

import abc


class InterfaceVeiculo(abc.ABC):

    @abc.abstractmethod
    def show_tipo(self):
        pass

class Carro(InterfaceVeiculo):

    def show_tipo(self):
        print('Carro')


class Moto(InterfaceVeiculo):

    def show_tipo(self):
        print('Moto')

# Coloque seu código aqui


if __name__ == "__main__":
    c = Carro()

    c.show_tipo()

    c = Moto()

    c.show_tipo()

"""

git clone https://github.com/treinaweb/treinaweb-python-algoritmos-parte1