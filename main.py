import streamlit as st
from GUI.side_bar import *

# Variaveis
valor_de_subtracao = 0
dado_de_dano = 0
dado_de_mult = 0
confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]


lista_npcs = criacao_npc([], valor_de_subtracao, dado_de_dano, dado_de_mult, confiabilidade_armar)

st.title("Cyberpunk")

st.text(lista_npcs)
