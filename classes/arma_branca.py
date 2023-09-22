class arma_branca():

    def __init__(self, nome,PA, precisao, dado_dano, tipo):
        self.nome = nome
        self.PA = PA
        self.tipo = tipo
        self.dado_dano = dado_dano
        self.precisao = precisao

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo
