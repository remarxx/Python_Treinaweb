class Animais:
    def __init__(self, tipo, qtde_patas, is_salvage, qtde_energia):
        self.__tipo = tipo
        self.__qtde_patas = qtde_patas
        self.__is_salvage = is_salvage
        self.__qtde_energia = qtde_energia
        self.__qtde_passos = 0
        self.__altura_pulo = 0
        self.__animal_awake = False

    def __del__(self):
        print('O objeto foi removido da memória')

    def andar_passos(self, qtde_passos):
        self.__qtde_passos += qtde_passos
        print(f'O animal andou {qtde_passos} passos')

    def pular(self, altura_pulo):
        self.__altura_pulo = altura_pulo
        print(f'O animal pulou a uma altura de {altura_pulo}cm ')

    def comer(self, qtde_energia):
        self.__qtde_energia += qtde_energia

    def acordar(self):
        if not self.__animal_awake:
            self.__animal_awake = True
            print('O animal acordou.')
        else:
            print('O animal já está acordado.')

    def dormir(self):
        if self.__animal_awake:
            self.__animal_awake = False
            print('O animal dormiu.')
        else:
            print('O animal já está dormindo.')
        print('O animal dormiu.')

    @property
    def tipos(self):
        return self.__tipo





