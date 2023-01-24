import animais

class Cachorro(animais.Animais):
    def __init__(self, tipo, qtde_patas, is_salvage, qtde_energia):
        super().__init__(tipo, qtde_patas, is_salvage, qtde_energia)
        self.raca_cachorro = 0
        self.nome_cachorro = 0
        self.idade_cachorro = 0
