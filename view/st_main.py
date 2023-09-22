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

    col1, col2, col3 = st.expander("Informações Personagem").columns(3)

    dict_d = {
        "Perícias": [pericia for pericia in pericias_classe(npc_escolhido.get_classe())],
        "Valor": [npc_escolhido.get_pericias()[pericia] for pericia in pericias_classe(npc_escolhido.get_classe())],
    }
    df = pd.DataFrame.from_dict(dict_d)
    col1.subheader("Perícias")
    col1.table(df)

    dict_d = {
        "Atributos": ['inteligencia', 'reflexo', 'tecnologia', 'auto controle', 'atratividade', 'sorte',
                      'movimento', 'tipo_corporal', 'empatia'],
        "Valor": [npc_escolhido.get_inteligencia(), npc_escolhido.get_reflexo(), npc_escolhido.get_tecnologia(),
                  npc_escolhido.get_auto_controle(), npc_escolhido.get_atratividade(), npc_escolhido.get_sorte(),
                  npc_escolhido.get_movimento(), npc_escolhido.get_tipo_corporal(), npc_escolhido.get_empatia()]
    }
    df = pd.DataFrame.from_dict(dict_d)
    col2.subheader("Atributos")
    col2.table(df)

    dict_d = {
        "Ciberwares": [ciberware.get_nome() for ciberware in npc_escolhido.get_cyberware() if ciberware != []]
    }
    df = pd.DataFrame.from_dict(dict_d)
    col3.subheader("Itens")
    col3.table(df)

    df = pd.DataFrame.from_dict({'Arma': [arma.get_nome() for arma in npc_escolhido.get_arma() if arma != []]})
    col3.table(df)

    st.divider()


def sistemas(npc, dificuldades):
    quantidade_tiros, buff_mira, debuff_mira, rd, pd = 0, 0, 0, 0, 0
    local = ''
    pericia_arma = 0
    dificuldade = 'Queima roupa - 10'
    sist_causar_dano, sist_receber_dano = st.tabs(["Sistema de dano", "Sistema de receber dano"])

    # Causar dano
    tipo, arma = selecione_informacoes_causar_dano(npc, sist_causar_dano)

    # tipo - 0 = arma de fogo
    # tipo - 1 = espingarda
    # tipo - 2 = maos vazia
    # tipo - 3 = arma branca

    # Dano com as armas de fogo
    if tipo == 0:

        tipo_arma = arma.get_tipo().lower()
        # Verificar a pericia que o npc tem com a arma
        if tipo_arma == 'pistola':
            pericia_arma = pega_pericia(npc, 'armas curtas'.lower())
        else:
            pericia_arma = pega_pericia(npc, tipo_arma.lower())

        buff_mira, debuff_mira, local = sistema_mira(sist_causar_dano, locais_corpo())

        quantidade_tiros = sist_causar_dano.number_input("Quantidade de tiros", min_value=1,
                                                         max_value=arma.get_tiros_por_turno())
        dificuldade = sist_causar_dano.selectbox("Selecione a dificuldade", dificuldades)

        # rola os dados
        # botao_rolar_dados(sist_causar_dano, npc, pericia_arma, dificuldades, dificuldade, local,
        #                   buff_mira, debuff_mira, quantidade_tiros=quantidade_tiros)


    # Dano com armas brancas
    elif tipo == 3:
        local = sist_causar_dano.selectbox("Local Atacado", locais_corpo())
        quantidade_tiros = 1
        # Pega a pontuação da pericia para arma branca
        pericia_arma = pega_pericia(npc, 'armas brancas'.lower())

        # to do precisa de um sistema de inventarioa e para verificar a lista as armas brancas q ele tem
        # mesma coisas para as armas a distancias

        sist_causar_dano.text("Dados do defensor")
        rd = sist_causar_dano.number_input('Reflexo', min_value=2, max_value=10)
        pd = sist_causar_dano.number_input('Pericias', min_value=0, max_value=10)
        sist_causar_dano.caption("Pode se usar a pericia de esquiva")

    # Sistema de rolagem de dados para definir o resultado
    if sist_causar_dano.button("Rolar dados"):
        # Resultado dos dados
        acertos, localTiroDic, resultado_final, resultado = botao_rolar_dados(sist_causar_dano, npc, arma, pericia_arma,
                                                                              dificuldades, dificuldade,
                                                                              local, buff_mira, debuff_mira,
                                                                              quantidade_tiros, rd, pd)
        metricas_sistema_receber_dano(sist_causar_dano, localTiroDic, resultado, resultado_final, acertos)


def pega_pericia(npc, pericia):
    # Pega a pontuação da pericia para arma branca
    for p in npc.get_pericias():
        if p == pericia:
            return int(npc.get_pericias()[p])
