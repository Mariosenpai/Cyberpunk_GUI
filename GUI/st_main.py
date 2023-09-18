import streamlit as st
from service import *


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


def sistema_mira(sist_causar_dano, local_corpo):
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


def sistemas(npc, local_corpo, dificuldades):
    sist_causar_dano, sist_receber_dano = st.tabs(["Sistema de dano", "Sistema de receber dano"])

    quantidade_tiros, dificuldade = selecione_informacoes_causar_dano(dificuldades, sist_causar_dano)

    buff_mira, debuff_mira, local = sistema_mira(sist_causar_dano, local_corpo)

    botao_rolar_dados(sist_causar_dano, npc, dificuldades, dificuldade, quantidade_tiros, local, buff_mira, debuff_mira)


# Botao para rola os dados
def botao_rolar_dados(sist_causar_dano, npc, dificuldades, dificuldade, quantidade_tiros, local, buff_mira,
                      debuff_mira):

    confiabilidade_armar = False


    if sist_causar_dano.button("Rolar dados"):

        # dicionario de todos os membros do corpo e seu dano causada a cada um deles
        localTiroDic = {'Cabeça': 0, 'Torso': 0, 'Braço direito': 0, 'Braço esquerdo': 0, 'Perna direita': 0,
                        'Perna esquerda': 0, }

        if npc.confiabilidade != "Não é uma arma automatica":
            confiabilidade_armar = True

        resultado_final, resultado  = rolagem_dado_causar_dano(npc,confiabilidade_armar, buff_mira,debuff_mira)

        valor_dificuldade = dificuldades[dificuldade]

        acertos, localTiroDic = sistema_tiros(npc, quantidade_tiros, resultado, resultado_final, sist_causar_dano,
                                              valor_dificuldade, localTiroDic, local)
        metricas_sistema_receber_dano(sist_causar_dano, localTiroDic, resultado, resultado_final, acertos)


# Mostra as todas as metricas relecionada ao causar dano
def metricas_sistema_receber_dano(sist_causar_dano, localTiroDic, resultado, resultado_final, acertos):
    col1, col2, col3 = sist_causar_dano.columns(3)
    col1.metric("Resultado Dados", value=resultado)
    col2.metric("Resultado Completo", value=resultado_final)
    col3.metric("Tiros Acertados", value=acertos)

    # Mostra todos os locais do corpo e seus repectivos danos recebido
    sist_causar_dano.write("Dano direciona as partes do corpo")
    for i, col in enumerate(sist_causar_dano.columns(len(locais_corpo()))):
        lc = locais_corpo()[i]
        col.metric(lc, localTiroDic[lc])


def rolagem_dado_causar_dano(npc,confiabilidade_armar, buff_mira,debuff_mira):
    resultado, falha = rolagem_dados_criticos(npc, confiabilidade_armar)
    return resultado + int(npc.REF) + int(npc.pericia_arma) + buff_mira - debuff_mira , resultado

def sistema_tiros(npc, quantidade_tiros, resultado, resultado_final, sist_causar_dano, valor_dificuldade,
                  localTiroDic, local):
    boleano_local_especifico = False
    acertos = 0

    # Se o local não for especificado entao ele o tiro vai ser em um local especifico
    if local != '':
        boleano_local_especifico = True

    if quantidade_tiros == 1:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = 1
            localTiroDic = resultado_tiros_acertados(npc, 1, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")

    elif quantidade_tiros == 3:
        resultado_final = resultado + 3
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = 3
            localTiroDic = resultado_tiros_acertados(npc, 3, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")

    elif quantidade_tiros > 3:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = resultado - valor_dificuldade

            if acertos > quantidade_tiros:
                acertos = quantidade_tiros

            localTiroDic = resultado_tiros_acertados(npc, acertos, localTiroDic,
                                                     boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    return acertos, localTiroDic


def selecione_informacoes_causar_dano(dificudades, sist_causar_dano):
    sist_causar_dano.subheader("Sistema de dano")
    sist_causar_dano.write("Ações do seu turno. Aqui iremos foca na ações relacionadas a ação de atirar")

    quantidade_tiros = sist_causar_dano.number_input("Quantidade de tiros", min_value=1, max_value=30)
    dificuldade = sist_causar_dano.selectbox("Selecione a dificuldade", dificudades)

    # arma_automatica = sist_causar_dano.toggle("Arma automatica")

    return quantidade_tiros, dificuldade
