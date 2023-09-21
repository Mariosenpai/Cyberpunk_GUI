from random import randint as random
from math import ceil
import os
import streamlit as st
import pickle
from .listas_e_dic import locais_corpo



def criar_personagem(npc, local_tela):
    with open(f'dados/npcs/NPC_{npc.nome}.pickle', 'wb') as arquivo:
        pickle.dump(npc, arquivo)
    arquivo.close()

    local_tela.success("NPC criado com sucesso!")

def preencher_automaticamente_pericias(pericia_escolhida):
    valor_max = 1
    # preencher os 40 ponto de forma aleatoria ate chega a 40 pontos
    while valor_max <= 40:
        for pericia in pericia_escolhida:
            if random(0, 1) == 1:
                pericia_escolhida[pericia] += 1
                valor_max += 1

    return pericia_escolhida

def pegaDificuldade(dificuldade):
    if dificuldade == 1:
        return 10
    elif dificuldade == 2:
        return 15
    elif dificuldade == 3:
        return 20
    elif dificuldade == 4:
        return 25
    else:
        return 30


def local_corpo_aleatorio():
    local = random(1, 10)

    if local == 1:
        return locais_corpo()[0]
    elif local in [2, 3, 4]:
        return locais_corpo()[1]
    elif local == 5:
        return locais_corpo()[2]
    elif local == 6:
        return locais_corpo()[3]
    elif local in [7, 8]:
        return locais_corpo()[4]
    else:
        return locais_corpo()[5]


def acertoResultado(npc, acertos, localTiroDic):
    for i in range(1, acertos + 1):
        # O local é aleatorio quando voce não especifica o mesmo
        local = local_corpo_aleatorio()
        localTiroDic = adiciona_dano_ao_local(npc, localTiroDic, local)
    # Qualquer dano na cabeca é dobrado
    localTiroDic['Cabeça'] *= 2
    return localTiroDic


def acertoResultadoLocalEspecifico(npc, acertos, localTiroDic, local):
    for i in range(1, acertos + 1):
        localTiroDic = adiciona_dano_ao_local(npc, localTiroDic, local)

    # Qualquer dano na cabeca é dobrado
    localTiroDic['Cabeça'] *= 2
    return localTiroDic


def calcula_dano(npc):
    dano = 0
    for i in range(npc.dado_de_mult):
        dano += random(1, npc.dado_de_dano)

    if (dano - npc.valor_de_subtracao) <= 0:
        return 1
    else:
        return dano - npc.valor_de_subtracao


def adiciona_dano_ao_local(npc, localTiroDic, local):
    dano = calcula_dano(npc)
    if local in localTiroDic:
        localTiroDic[local] += dano
    else:
        localTiroDic[local] = dano
    return localTiroDic


def escolhe_local(id_local):
    local = local_corpo_aleatorio()

    return local[id_local - 1]


def resultado_tiros_acertados(npc, acertos, localTiroDic, boleano_local_especifico=False, local=''):
    if not boleano_local_especifico:
        return acertoResultado(npc, acertos, localTiroDic)
    else:
        return acertoResultadoLocalEspecifico(npc, acertos, localTiroDic, local)


def armar_falhou(confiabilidade):
    confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]

    evitar_falha = random(1, 10)
    if confiabilidade == confiabilidade_armar[1]:
        if evitar_falha <= 8:
            return True
    if confiabilidade == confiabilidade_armar[2]:
        if evitar_falha <= 5:
            return True
    if confiabilidade <= confiabilidade_armar[3]:
        return True


def tipos_falha_criticas(npc):
    tipo_falha_critica = random(1, 10)

    if tipo_falha_critica <= 4:
        st.text("Nada acontece...")
        return False
    elif tipo_falha_critica == 5:
        st.text("Voce deixa sua arma cair")
        return True
    elif tipo_falha_critica == 6:
        st.text("Atinge algo inofencivo sem ser o alvo")
        return True
    elif tipo_falha_critica == 7:
        st.text("Arma trava")
        return True
    elif tipo_falha_critica == 8:
        st.text(f"Voce se atira na/o {local_corpo_aleatorio()}")
        st.text(f"Levou {calcula_dano(npc)} de dano no local")
        return True
    elif tipo_falha_critica >= 9:
        st.text("Voce atinge um membro do grupo")
        st.text("Todo o dano a parte de agora em diante será direicionado para um membro de o grupo")
        return False


def rolagem_dados_criticos(npc, automatica):
    resultado_dado = random(1, 10)
    falha = False

    st.text(f"log:\nResultado do dado = {resultado_dado}")
    if resultado_dado == 10:
        st.text("ACERTO CRITICO!! \nrolagem de dado adicional")
        nova_rolagem = random(1, 10)
        st.text(f"Resultado da nova rolagem = {nova_rolagem}")
        resultado_dado += nova_rolagem
        st.text(f"Resultado final do dado = {resultado_dado}")
    elif resultado_dado == 1:
        st.text("FALHA CRITICA!!")
        if automatica:
            falha = armar_falhou(npc.confiabilidade)
        else:
            falha = tipos_falha_criticas(npc)

    return resultado_dado, falha


def pegaCaminhoArquivos(pasta_principal):
    caminho_dic = {}
    lista_arquivos = []

    # Itera sobre os diretórios dentro da pasta principal
    for diretorio in os.listdir(pasta_principal):
        # Verifica se o item é um diretório
        if os.path.isdir(os.path.join(pasta_principal, diretorio)):
            # Obtém o caminho completo para o diretório
            caminho_diretorio = os.path.join(pasta_principal, diretorio)
            # Itera sobre os arquivos dentro do diretório
            for arquivo in os.listdir(caminho_diretorio):
                # Verifica se o item é um arquivo
                if os.path.isfile(os.path.join(caminho_diretorio, arquivo)):
                    # Imprime o caminho completo do arquivo
                    caminho_arquivo = os.path.join(caminho_diretorio, arquivo)
                    lista_arquivos.append(caminho_arquivo)
        caminho_dic.update({diretorio: lista_arquivos})
        lista_arquivos = []

    return caminho_dic
