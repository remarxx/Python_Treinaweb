import animais


class Gato(animais.Animais):
    def __init__(self, tipo, qtde_patas, is_salvage, qtde_energia):
        super().__init__(tipo, qtde_patas, is_salvage, qtde_energia)
        self.raca_gato = 0
        self.nome_gato = 0
        self.idade_gato = 0
