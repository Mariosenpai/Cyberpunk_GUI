from service.service import *
from service.sistema_dano import *


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


def selecione_informacoes_causar_dano(npc, sist_causar_dano):
    sist_causar_dano.subheader("Sistema de dano")
    sist_causar_dano.write("Ações que seu personagem pode fazer.")

    # transforma a lista de arma em um dicinario onde a chave é o nome e o valor o objeto
    dic_arma = {}
    for a in npc.get_arma():
        dic_arma[a.get_nome()] = a

    # O selectbox irar retorna apenas a chave do dicionario
    arma_nome = sist_causar_dano.selectbox("Escolher Arma", dic_arma)
    # seleciona o objeto atraves da chave dada pelo selectbox e pego seu tipo
    tipo_arma = dic_arma[arma_nome].get_tipo()

    arma = dic_arma[arma_nome]

    sist_causar_dano.caption(f"Tipo {tipo_arma}")

    espingarda = tipos_arma()[3]
    arma_branca = tipos_arma()[6]
    maos_vazia = tipos_arma()[7]

    # Se ela não for uma arma branca espingarda e de maos vazia
    if not (tipo_arma in [arma_branca, espingarda, maos_vazia]):
        return 0, arma
    # Dependendo do tipo de arma ela tera uma laucher especifico
    elif tipo_arma == espingarda:
        return 1, arma
    elif tipo_arma == maos_vazia:
        return 2, arma
    # Arma branca
    else:
        return 3, arma

    # arma_automatica = sist_causar_dano.toggle("Arma automatica")
