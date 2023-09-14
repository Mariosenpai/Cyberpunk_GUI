import streamlit as st
import pickle
from service import pegaCaminhoArquivos
from GUI.side_bar import *

# Variaveis
valor_de_subtracao = 0
dado_de_dano = 0
dado_de_mult = 0
confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]


criacao_npc(valor_de_subtracao, dado_de_dano, dado_de_mult, confiabilidade_armar)

st.title("Cyberpunk")

if st.sidebar.button("Busca npcs salvos"):
    lista_npcs = []
    caminho_dic = pegaCaminhoArquivos("dados")
    for npc_salvo in caminho_dic:
        with open(f"dados/{npc_salvo}", 'rb') as arquivo_aberto:
            lista_npcs.append(pickle.load(arquivo_aberto))

    for n in lista_npcs:
        st.text(f"Nome: {n.nome}\n"
                f"Reflexo(REF): {n.REF}\n"
                f"Pericia com a arma: {n.pericia_arma}\n"
                f"Dado de dano da arma: {n.dado_full}")
