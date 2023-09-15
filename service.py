from random import randint as random
from math import ceil
import os
import streamlit as st


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


def localCorpo():
    local = random(1, 10)

    if local == 1:
        return 'cabeca'
    elif local in [2, 3, 4]:
        return 'torso'
    elif local == 5:
        return 'braco direito'
    elif local == 6:
        return 'braco esquerdo'
    elif local in [7, 8]:
        return 'perna direita'
    else:
        return 'perna esquerda'


def acertoResultado(acertos, localTiroDic):
    for i in range(1, acertos + 1):
        # O local é aleatorio quando voce não especifica o mesmo
        local = localCorpo()
        localTiroDic = adiciona_dano_ao_local(localTiroDic, local)
    # Qualquer dano na cabeca é dobrado
    localTiroDic['cabeca'] *= 2
    print(localTiroDic)


def acertoResultadoLocalEspecifico(acertos, localTiroDic, local):
    for i in range(1, acertos + 1):
        localTiroDic = adiciona_dano_ao_local(localTiroDic, local)

    # Qualquer dano na cabeca é dobrado
    localTiroDic['cabeca'] *= 2
    print(localTiroDic)


def calcula_dano(npc):
    dano = 0
    for i in range(npc.dado_de_mult):
        dano += random(1, npc.dado_de_dano)

    if (dano - npc.valor_de_subtracao) <= 0:
        return 1
    else:
        return dano - npc.valor_de_subtracao


def adiciona_dano_ao_local(localTiroDic, local):
    dano = calcula_dano()
    if local in localTiroDic:
        localTiroDic[local] += dano
    else:
        localTiroDic[local] = dano
    return localTiroDic


def escolhe_local(id_local):
    local = ['cabeca', 'torso', 'braco direito', 'braco esquerdo', 'perna direita', 'perna esquerda']

    return local[id_local - 1]


def resultado_tiros_acertados(acertos, localTiroDic, boleano_local_especifico=False, local=''):
    if not boleano_local_especifico:
        acertoResultado(acertos, localTiroDic)
    else:
        acertoResultadoLocalEspecifico(acertos, localTiroDic, local)


def armar_falhou(confiabilidade):
    confiabilidade_armar = ["Não é uma arma automatica", "Pouco confiavel", "Padrão", "Muito confiavel"]

    evitar_falha = random(1, 10)
    if confiabilidade == confiabilidade_armar[1]:
        if evitar_falha <= 8:
            print("Armar falhou")
            return True
    if confiabilidade == confiabilidade_armar[2]:
        if evitar_falha <= 5:
            print("Armar falhou")
            return True
    if confiabilidade <= confiabilidade_armar[3]:
        print("Armar falhou")
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
        st.text(f"Voce se atira na/o {localCorpo()}")
        st.text(f"Levou {calcula_dano(npc)} de dano no local")
        return True
    elif tipo_falha_critica >= 9:
        st.text("Voce atinge um membro do grupo")
        st.text("Todo o dano a parte de agora em diante será direicionado para um membro de o grupo")
        return False


def rolagem_dados_criticos(npc, automatica):
    resultado_dado = random(1,10)
    falha = False
    st.text(f"Resultado do dado = {resultado_dado}")
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
