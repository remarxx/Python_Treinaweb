import veiculo


class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtde_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe carro.')
        self._qtd_combustivel = qtd_combustivel

    def pintar(self, cor):
        if cor == 'Preto' or 'preto':
            print('O carro não pode ser preto.')
        else:
            self._cor = cor

