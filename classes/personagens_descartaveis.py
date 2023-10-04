from random import randint as random


def atributo_aleatorio(limitador, limite):
    resultado = random(1, 6) + random(1, 6)
    if limitador:
        if resultado >= limite:
            return limite
    else:
        return resultado


class personagem_descatavel:
    def __init__(self,classe, nome, inteligencia=2, reflexo=2, tecnologia=2, auto_controle=2, atratividade=2, sorte=2,
                 movimento=2, tipo_corporal=2, empatia=2, preencher_automatico=True, limitador=False, limite=11):
        self.nome = nome
        self.personagem_descatavel = True
        self.classe = classe
        self.arma = []

        if preencher_automatico:
            self.inteligencia = atributo_aleatorio(limitador, limite)
            self.reflexo = atributo_aleatorio(limitador, limite)
            self.tecnologia = atributo_aleatorio(limitador, limite)
            self.auto_controle = atributo_aleatorio(limitador, limite)
            self.atratividade = atributo_aleatorio(limitador, limite)
            self.sorte = atributo_aleatorio(limitador, limite)
            self.movimento = atributo_aleatorio(limitador, limite)
            self.tipo_corporal = atributo_aleatorio(limitador, limite)
            self.empatia = atributo_aleatorio(limitador, limite)
        else:
            self.inteligencia = inteligencia
            self.reflexo = reflexo
            self.tecnologia = tecnologia
            self.auto_controle = auto_controle
            self.atratividade = atratividade
            self.sorte = sorte
            self.movimento = movimento
            self.tipo_corporal = tipo_corporal
            self.empatia = empatia

    # Funções getter para obter os valores dos atributos

    def remover_arma(self, nome_arma):
        if nome_arma == 'Nenhum':
            return False
        for i,a in enumerate(self.arma):
            if a.get_nome() == nome_arma:
                self.arma.remove(a)
                return True
            else:
                return False

    def remover_ciberware(self, nome_ciberware):
        print('ah pora' ,self.cyberware)
        for i,c in enumerate(self.cyberware):
            if c.get_nome() == nome_ciberware:
                self.cyberware.remove(c)
                return True
            else:
                return False

    def add_arma(self,arma):
        self.arma.append(arma)

    def get_arma(self):
        return self.arma

    def add_cyberwares(self, cyberware):
        self.cyberware = cyberware

    def get_cyberware(self):
        return self.cyberware

    def modificador_tipo_corporal(self):
        if self.tipo_corporal == 2:
            return 'Muito Fraco'
        elif self.tipo_corporal in [3,4]:
            return 'Fraco'
        elif self.tipo_corporal in [5,7]:
            return 'Medio'
        elif self.tipo_corporal in [8,7]:
            return 'Forte'
        elif self.tipo_corporal == 10:
            return 'Muito Forte'
    def todos_atributos_lits(self):
        return {"inteligencia": self.inteligencia, "reflexo": self.reflexo, "tecnologia": self.tecnologia,
                "auto controle": self.auto_controle, "atratividade": self.atratividade, "sorte": self.sorte,
                "movimento": self.movimento, "tipo corporal": self.tipo_corporal, "empatia": self.empatia}

    def add_pericias(self, pericias):
        self.pericias = pericias

    def get_pericias(self):
        return self.pericias

    def get_personagem_descartavel(self):
        return personagem_descatavel

    def get_classe(self):
        return self.classe

    def get_nome(self):
        return self.nome

    def get_inteligencia(self):
        return self.inteligencia

    def get_reflexo(self):
        return self.reflexo

    def get_tecnologia(self):
        return self.tecnologia

    def get_auto_controle(self):
        return self.auto_controle

    def get_atratividade(self):
        return self.atratividade

    def get_sorte(self):
        return self.sorte

    def get_movimento(self):
        return self.movimento

    def get_tipo_corporal(self):
        return self.tipo_corporal

    def get_empatia(self):
        return self.empatia

    # Funções setter para definir os valores dos atributos
    def set_nome(self, nome):
        self.nome = nome

    def set_inteligencia(self, inteligencia):
        self.inteligencia = inteligencia

    def set_reflexo(self, reflexo):
        self.reflexo = reflexo

    def set_tecnologia(self, tecnologia):
        self.tecnologia = tecnologia

    def set_auto_controle(self, auto_controle):
        self.auto_controle = auto_controle

    def set_atratividade(self, atratividade):
        self.atratividade = atratividade

    def set_sorte(self, sorte):
        self.sorte = sorte

    def set_movimento(self, movimento):
        self.movimento = movimento

    def set_tipo_corporal(self, tipo_corporal):
        self.tipo_corporal = tipo_corporal

    def set_empatia(self, empatia):
        self.empatia = empatia
