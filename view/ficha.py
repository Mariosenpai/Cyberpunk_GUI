import streamlit as st
from service.service import *
from service.pericias import pericias_classe
from classes.personagens_descartaveis import *
from service.listas_e_dic import *
from classes.ciberware import ciberware
from classes.arma_branca import *
from classes.arma_de_fogo import *


def ficha_npc(npc_escolhido):
    st.subheader("Ficha do NPC")
    st.text(f"Nome: {npc_escolhido.nome}\n"
            f"Reflexo(REF): {npc_escolhido.REF}\n"
            f"Pericia com a arma: {npc_escolhido.pericia_arma}\n"
            f"Dado de dano da arma: {npc_escolhido.dado_full}\n"
            f"Automatica: {npc_escolhido.confiabilidade}")


def criar_personagens_descataveis():
    pd = st.sidebar.expander("Personagens Descartaveis")

    nome = pd.text_input("Nome")
    classe = pd.selectbox("Classes", classes())
    npc = personagem_descatavel(nome=nome, classe=classe)
    pd.caption("Armas e cyberware seram gerados automaticamente de acordo com a regra do jogo")
    pericia_escolhida, boleano_pericia = pericias(pd, classe)

    # Verifica se pode liberar o botao para criar o personagem
    if boleano_pericia:
        st.warning("O valor maximo para todas as pericias é 40")
    else:
        botao_criar_personagem(pd, npc, pericia_escolhida)
    # pd.text("Atributos gerados automaticamente")
    # for i, col in enumerate(pd.columns(len(atributos()))):
    #     valor_atr = atributos()[i]
    #     col.metric(valor_atr, atributos_personagem[valor_atr])


def pericias(pd, classe):
    valor_max_pericias = 40
    valor_pericas = 0
    max_pericia = False

    pericia_escolhida = pericias_classe(classe)
    pd.subheader(f"Pericias da classe {classe}")

    if pd.toggle("Preencher pericias automaticamente", True):
        return preencher_automaticamente_pericias(pericia_escolhida), max_pericia

    else:
        # Escolher pericias
        for i, pericia in enumerate(pericia_escolhida):
            pericia_escolhida[pericia] = pd.number_input(pericia, min_value=0, max_value=10)
            valor_pericas += pericia_escolhida[pericia]

        if valor_max_pericias < valor_pericas:
            max_pericia = True

        return pericia_escolhida, max_pericia


def botao_criar_personagem(local, npc, pericia_escolhida):
    if local.button("Criar personagem"):
        npc.add_pericias(pericia_escolhida)

        npc_aux = adiciona_ciberwares(npc)

        npc_final = adiciona_arma(npc_aux)

        criar_personagem(npc_final, st)


def adiciona_arma(npc):
    # arma branca
    if random(0, 1) == 0:
        item_ar = seleciona_aleatoriamente_arma(lista_armas_brancas(), 'ab')
    else:
        item_ar = seleciona_aleatoriamente_arma(lista_armas_de_fogo(), 'af')

    print("arma a ser adicionada ", item_ar)
    # Adiciona a arma obs: so pode ter uma arma
    # Salvando como uma lista
    npc.add_arma(item_ar)

    return npc


def adiciona_ciberwares(npc):
    # definir os itens/armas e cyberware do npc
    todos_ciberwares = []

    # ciberopticos
    item_co = seleciona_aleatoriamente_ciberware(lista_ciberware_opticos())

    # ciberaudio
    item_au = seleciona_aleatoriamente_ciberware(lista_ciberware_audio())

    # Tem 50% de chances de ele ter ou não um impante neural
    item_n = []
    if random(0, 1) == 1:
        item_n = seleciona_aleatoriamente_ciberware(lista_ciberware_neurais())

    todos_ciberwares.append(item_co)
    todos_ciberwares.append(item_au)
    todos_ciberwares.append(item_n)

    # Adiciona os ciberware
    npc.add_cyberwares(todos_ciberwares)

    return npc


def seleciona_aleatoriamente_ciberware(lista_ciberware):
    list_c = []
    # Lista de ciberware cadastrados
    for c in lista_ciberware:
        list_c.append(c.split(','))

    # cria um ciberware e adiciona um aleatoriamente no NPC
    return criar_ciberware(list_c[random(0, len(list_c) - 1)])


# af = arma de fogo
# ab = arma branca
# ax = arma exotica
# al = arma a laser
def seleciona_aleatoriamente_arma(lista_armas, tipo='af'):
    lista_a = []
    for a in lista_armas:
        lista_a.append(a.split(','))

    arma_selecionada = lista_a[random(0, len(lista_a) - 1)]
    print("arma = ",arma_selecionada)

    if tipo == 'ab':
        return criar_arma_branca(arma_selecionada)
    elif tipo == 'af':
        return criar_arma_de_fogo(arma_selecionada)


# Armas
def criar_arma_de_fogo(item_arma):
    return arma_de_fogo(item_arma[0], int(item_arma[1]), item_arma[2], int(item_arma[3]), int(item_arma[4]), int(item_arma[5]),
                        item_arma[6], '')


def criar_arma_branca(item_arma):
    return arma_branca(item_arma[0], int(item_arma[1]), item_arma[2], item_arma[3], "Arma Branca")


# Armas

# Cria o objeto cyberware
def criar_ciberware(item_ciberware):
    return ciberware(item_ciberware[0], int(item_ciberware[1]), item_ciberware[2])
