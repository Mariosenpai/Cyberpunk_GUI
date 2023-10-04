class arma_de_fogo:

    def __init__(self, nome, PA, dado_dano, quantidade_balas, tiros_por_turno, alcance, tipo, descricao):
        self.nome = nome
        self.dado_dano = dado_dano
        self.quantidade_balas = quantidade_balas
        self.tiros_por_turno = tiros_por_turno
        self.alcance = alcance
        self.tipo = tipo
        self.PA = PA
        self.descricao = descricao

    def get_PA(self):
        return self.PA
    def get_quantidade_balas(self):
        return self.quantidade_balas

    def set_quantidade_balas(self, valor):
        self.quantidade_balas = valor

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo

    def get_tiros_por_turno(self):
        return self.tiros_por_turno

    def get_descricao(self):
        return self.descricao
