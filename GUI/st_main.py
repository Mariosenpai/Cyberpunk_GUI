import streamlit as st
from service import *


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


def sistema_mira(sist_causar_dano,local_corpo):
    local = ''
    buff_mira = 0
    debuff_mira = 0

    if sist_causar_dano.toggle("Mirar"):
        sist_causar_dano.write("Mirar em um local especifico do corpo da um debuff de - 4")
        if sist_causar_dano.toggle("Local especifico"):
            local = sist_causar_dano.selectbox("Local mirado", local_corpo)
            debuff_mira = 4
        else:
            sist_causar_dano.write("Mira da um buff de ate 3 na precisão")
            turnos_mirando = sist_causar_dano.number_input("Turnos mirando", min_value=1)

            if turnos_mirando > 3:
                buff_mira = 3
            else:
                buff_mira = turnos_mirando
    return buff_mira, debuff_mira, local

def selecione_informacoes(npc, local_corpo, dificudades):

    sist_causar_dano, sist_receber_dano = st.tabs(["Sistema de dano", "Sistema de receber dano"])

    sist_causar_dano.subheader("Sistema de dano")
    sist_causar_dano.write("Ações do seu turno. Aqui iremos foca na ações relacionadas a ação de atirar")

    quantidade_tiros = sist_causar_dano.number_input("Quantidade de tiros", min_value=1, max_value=30)
    dificuldade = sist_causar_dano.selectbox("Selecione a dificuldade", dificudades)

    arma_automatica = sist_causar_dano.toggle("Arma automatica")

    buff_mira, debuff_mira, local = sistema_mira(sist_causar_dano, local_corpo)

    if sist_causar_dano.button("Rolar dados"):
        resultado, falha = rolagem_dados_criticos(npc, arma_automatica)

        resultado_final = resultado + buff_mira - debuff_mira

        return quantidade_tiros, dificuldade, local, resultado_final
    else:
        return None, None, None, None
