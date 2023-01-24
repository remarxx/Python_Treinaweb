import abc
import interface_Veiculo


class Veiculo(interface_Veiculo.InterfaceVeiculo, abc.ABC):
    """Essa é a classe carro. Esta classe é utilizada para instanciar novos carros em nosso programa."""

    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = 0
        self.__velocidade = 0

    def __del__(self):
        print(
            'O objeto foi removido da memória'
        )

    def pintar(self, cor):
        self._cor = cor
        print('O veícuilo está com a cor', self._cor)

    @property
    def cor(self):
        return self._cor

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo
        qtd_combustivel do objeto. """
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print('O carro já está ligado')
        else:
            self.__is_ligado = True
            print('O carro foi ligado')

    def desligar(self):
        if not self.__is_ligado:
            print('O carro já está desligado')
        else:
            self.__is_ligado = False

    def acelerar(self, velocidade):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('O carro precisa estar ligado para ser acelerado')
