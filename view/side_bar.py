import pickle
from classes import classe_npc
from .st_main import *
from service.service import *
from view.ficha import *


def criacao_npc(valor_de_subtracao, dado_de_dano, dado_de_mult, confiabilidade_armar):
    side = st.sidebar

    # Criar um novo npc
    criar_npc = side.expander("Adicionar novo NPC")

    nome = criar_npc.text_input("Nome")
    REF = criar_npc.text_input("Reflexo")
    pericia_armar = criar_npc.text_input("Pericia com a armar")
    dado_dano = criar_npc.text_input("dado de dano. Ex: 1d6, 2d6-1")
    confiabilidade_selecionada = criar_npc.selectbox("Selecione a confiabilidade da armar", confiabilidade_armar)

    if criar_npc.button("Salva"):

        if 3 < len(dado_dano) <= 5:
            valor_de_subtracao = int(dado_dano[4])
            dado_de_dano = int(dado_dano[2])
            dado_de_mult = int(dado_dano[0])
        elif len(dado_dano) <= 3:
            dado_de_dano = int(dado_dano[2])
            dado_de_mult = int(dado_dano[0])

        npc = classe_npc.npc(nome, REF, pericia_armar, valor_de_subtracao, dado_de_dano, dado_de_mult,
                             confiabilidade_selecionada, dado_dano)

        # salva npc em um arquivo
        criar_personagem(npc, side)

    # Criar um novo npc

