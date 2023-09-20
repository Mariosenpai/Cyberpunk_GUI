import streamlit as st
from service.service import *
from service.pericias import pericias_classe
from classes.personagens_descartaveis import *


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


def ficha_personagem_descartavel(npc_escolhido):
    st.subheader("Ficha de Personagem descartavel")

    st.divider()
    st.write(f"Nome : {npc_escolhido.get_nome()}")
    st.write(f"Classe : {npc_escolhido.get_classe()}")

    st.divider()

    col1, col2 = st.columns(2)

    col1.write("PERICIAS")
    for i, pericia in enumerate(pericias_classe(npc_escolhido.get_classe())):
        col1.write(f"{pericia} :{npc_escolhido.get_pericias()[pericia]}")


    st.divider()


def criar_personagens_descataveis():
    pd = st.sidebar.expander("Personagens Descartaveis")


    nome = pd.text_input("Nome")
    classe = pd.selectbox("Classes", classes())
    npc = personagem_descatavel(nome=nome,classe=classe)
    pd.caption("Armas e cyberware seram gerados automaticamente de acordo com a regra do jogo")
    pericias(pd, npc)

    # pd.text("Atributos gerados automaticamente")
    # for i, col in enumerate(pd.columns(len(atributos()))):
    #     valor_atr = atributos()[i]
    #     col.metric(valor_atr, atributos_personagem[valor_atr])


def pericias(pd, npc):
    #classe padrao
    classe = 'solo'
    valor_max_pericias = 40
    valor_pericas = 0

    pd.subheader(f"Pericias da classe {classe}")
    pericia_escolhida = pericias_classe(classe)

    if pd.toggle("Preencher pericias automaticamente", True):
        pericia_escolhida = preencher_automaticamente_pericias(pericia_escolhida)
        botao_criar_personagem(pd, npc, pericia_escolhida)
    else:
        # Escolher pericias
        for i, pericia in enumerate(pericia_escolhida):
            pericia_escolhida[pericia] = pd.number_input(pericia, min_value=0, max_value=10)
            valor_pericas += pericia_escolhida[pericia]

        if valor_max_pericias < valor_pericas:
            st.warning("O valor maximo para todas as pericias é 40")
        else:
            botao_criar_personagem(pd, npc, pericia_escolhida)

def botao_criar_personagem(local,npc,pericia_escolhida):
    if local.button("Criar personagem"):
        npc.add_pericias(pericia_escolhida)
        criar_personagem(npc, st)