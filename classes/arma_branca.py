class arma_branca():

    def __init__(self, nome,PA, dado_dano,descricao, tipo):
        self.nome = nome
        self.PA = PA
        self.descricao = descricao
        self.tipo = tipo
        self.dado_dano = dado_dano

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo
