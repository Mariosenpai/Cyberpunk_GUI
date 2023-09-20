import streamlit as st
import pickle
from view.side_bar import *
from view.st_main import *
from view.ficha import *
from service.service import *

# Variaveis
valor_de_subtracao = 0
dado_de_dano = 0
dado_de_mult = 0
buff_mira = 0
debuff_mira = 0

confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]
dificudades = {"Queima roupa - 10": 10, "Curta distancia - 15": 15,
               "Media distancia - 20": 20, "longa distancia - 25": 25, "Exterma distancia - 30": 30}

st.title("Cyberpunk")




# SIDEBAR
#criacao_npc(valor_de_subtracao, dado_de_dano, dado_de_mult, confiabilidade_armar)
criar_personagens_descataveis()
npc = buscar_npc()
pericia_arma = 10
sistemas(npc,pericia_arma , dificudades)
