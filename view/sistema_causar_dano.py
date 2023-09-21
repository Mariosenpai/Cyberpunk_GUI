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


def selecione_informacoes_causar_dano(dificudades, sist_causar_dano):
    sist_causar_dano.subheader("Sistema de dano")
    sist_causar_dano.write("Ações do seu turno. Aqui iremos foca na ações relacionadas a ação de atirar")

    tipo_arma = sist_causar_dano.selectbox("Tipo arma", tipos_arma())

    espingarda = tipos_arma()[3]
    arma_branca = tipos_arma()[6]
    maos_vazia = tipos_arma()[7]

    # Dependendo do tipo de arma ela tera uma laucher especifico
    if tipo_arma == arma_branca:
        return 0
    # Se ela não for uma arma branca espingarda e de maos vazia
    elif not (tipo_arma in [arma_branca, espingarda, maos_vazia]):
        return 1
    elif tipo_arma == espingarda:
        return 2
    else:
        return 3

    # arma_automatica = sist_causar_dano.toggle("Arma automatica")
