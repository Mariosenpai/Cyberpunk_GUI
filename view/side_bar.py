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


def buscar_npc():
    lista_npcs = {}
    caminho_dic = pegaCaminhoArquivos("dados/npcs")
    for npc_salvo in caminho_dic:

        with open(f"dados/npcs/{npc_salvo}", 'rb') as arquivo_aberto:
            npc = pickle.load(arquivo_aberto)
            lista_npcs[npc.nome] = npc

    npc_escolhido = st.sidebar.selectbox("Busca npcs salvos", lista_npcs)
    # for npc_escolhido in lista_npcs:
    if len(lista_npcs) == 0:
        return st.text('Sem personagem cadastrado')

    npc_escolhido = lista_npcs[npc_escolhido]
    if npc_escolhido.get_personagem_descartavel:
        ficha_personagem_descartavel(npc_escolhido)
    else:
        ficha_npc(npc_escolhido)

    return npc_escolhido
