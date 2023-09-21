import streamlit as st
from math import ceil
from service import *
from .sistema_causar_dano import *
from service.sistema_dano import *
from .sistema_armas_de_fogo import *


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


def sistemas(npc, dificuldades):
    quantidade_tiros,buff_mira, debuff_mira= 0,0,0
    local = ''

    sist_causar_dano, sist_receber_dano = st.tabs(["Sistema de dano", "Sistema de receber dano"])

    # Causar dano
    tipo = selecione_informacoes_causar_dano(dificuldades,sist_causar_dano)

    if tipo == 0:
        local = sist_causar_dano.selectbox("Local Atacado", locais_corpo())
        # to do precisa de um sistema de inventarioa e para verificar a lista as armas brancas q ele tem
        # mesma coisas para as armas a distancias



    # Dano com as armas
    elif tipo == 1:
        buff_mira, debuff_mira, local = sistema_mira(sist_causar_dano, locais_corpo())

        quantidade_tiros = sist_causar_dano.number_input("Quantidade de tiros", min_value=1, max_value=30)
        dificuldade = sist_causar_dano.selectbox("Selecione a dificuldade", dificuldades)

    #rola os dados
    # botao_rolar_dados(sist_causar_dano, npc, pericia_arma, dificuldades, dificuldade, local,
    #                   buff_mira, debuff_mira, quantidade_tiros=quantidade_tiros)

    if sist_causar_dano.button("Rolar dados"):
        # Resultado dos dados
        acertos, localTiroDic, resultado_final, resultado = botao_rolar_dados(sist_causar_dano, npc, pericia_arma,
                                                                              dificuldades, dificuldade,
                                                                              quantidade_tiros, local,
                                                                              buff_mira, debuff_mira)
        metricas_sistema_receber_dano(sist_causar_dano, localTiroDic, resultado, resultado_final, acertos)
