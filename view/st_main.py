import streamlit as st
from math import ceil
from service import *
from .sistema_causar_dano import *
from service.sistema_dano import *
from .sistema_armas_de_fogo import *
from service.pericias import pericias_classe
import pandas as pd


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


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


def ficha_personagem_descartavel(npc_escolhido):
    st.subheader("Ficha de Personagem descartavel")

    st.divider()
    st.write(f"Nome : {npc_escolhido.get_nome()}")
    st.write(f"Classe : {npc_escolhido.get_classe()}")

    st.divider()

    col1, col2 = st.expander("Informações Personagem").columns(2)

    dict_d = {
        "Perícias": [pericia for pericia in pericias_classe(npc_escolhido.get_classe())],
        "Valores": [npc_escolhido.get_pericias()[pericia] for pericia in pericias_classe(npc_escolhido.get_classe())],
    }
    df = pd.DataFrame.from_dict(dict_d)
    col1.subheader("Perícias")
    col1.table(df)

    dict_d = {
        "Ciberwares": [ciberware.get_nome() for ciberware in npc_escolhido.get_cyberware() if ciberware != []]
    }
    df = pd.DataFrame.from_dict(dict_d)
    col2.subheader("Itens")
    col2.table(df)


    print(npc_escolhido.get_arma())
    df = pd.DataFrame.from_dict({'Arma': [arma.get_nome() for arma in npc_escolhido.get_arma() if arma != []]})
    col2.table(df)

    st.divider()


def sistemas(npc, dificuldades):
    quantidade_tiros, buff_mira, debuff_mira = 0, 0, 0
    local = ''

    sist_causar_dano, sist_receber_dano = st.tabs(["Sistema de dano", "Sistema de receber dano"])

    # Causar dano
    tipo, arma = selecione_informacoes_causar_dano(npc, sist_causar_dano)

    # tipo - 0 = arma de fogo
    # tipo - 1 = espingarda
    # tipo - 2 = maos vazia
    # tipo - 3 = arma branca

    # Dano com as armas
    if tipo == 0:
        buff_mira, debuff_mira, local = sistema_mira(sist_causar_dano, locais_corpo())
        print(arma.get_tiros_por_turno())
        quantidade_tiros = sist_causar_dano.number_input("Quantidade de tiros", min_value=1,
                                                         max_value=arma.get_tiros_por_turno())
        dificuldade = sist_causar_dano.selectbox("Selecione a dificuldade", dificuldades)

        # rola os dados
        # botao_rolar_dados(sist_causar_dano, npc, pericia_arma, dificuldades, dificuldade, local,
        #                   buff_mira, debuff_mira, quantidade_tiros=quantidade_tiros)

        if sist_causar_dano.button("Rolar dados"):
            # Resultado dos dados
            acertos, localTiroDic, resultado_final, resultado = botao_rolar_dados(sist_causar_dano, npc, pericia_arma,
                                                                                  dificuldades, dificuldade,
                                                                                  quantidade_tiros, local,
                                                                                  buff_mira, debuff_mira)
            metricas_sistema_receber_dano(sist_causar_dano, localTiroDic, resultado, resultado_final, acertos)

    elif tipo == 3:
        local = sist_causar_dano.selectbox("Local Atacado", locais_corpo())
        # to do precisa de um sistema de inventarioa e para verificar a lista as armas brancas q ele tem
        # mesma coisas para as armas a distancias
