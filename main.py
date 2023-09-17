import streamlit as st
import pickle
from GUI.side_bar import *
from GUI.st_main import *
from service import *

# Variaveis
valor_de_subtracao = 0
dado_de_dano = 0
dado_de_mult = 0
buff_mira = 0
debuff_mira = 0

confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]
dificudades = {"Queima roupa - 10": 10, "Curta distancia - 15": 15,
               "Media distancia - 20": 20, "longa distancia - 25": 25, "Exterma distancia - 30": 30}
local_corpo = locais_corpo()

st.title("Cyberpunk")

# SIDEBAR
criacao_npc(valor_de_subtracao, dado_de_dano, dado_de_mult, confiabilidade_armar)
npc = buscar_npc()
sistemas(npc, local_corpo, dificudades)
