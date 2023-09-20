from .service import *


def sistema_arma_branco():
    pass

def sistema_dano_fisico(npc):
    modicador_dano = dic_tipo_corporal_dano()[npc.modificador_tipo_corporal()]

# Botao para rola os dados
def botao_rolar_dados(sist_causar_dano, npc, pericia_arma, dificuldades, dificuldade, local,
                      buff_mira, debuff_mira,quantidade_tiros=0):
    confiabilidade_armar = False


    if npc.confiabilidade != "Não é uma arma automatica":
        confiabilidade_armar = True

    resultado_final, resultado = rolagem_dado_causar_dano(npc, pericia_arma, confiabilidade_armar, buff_mira,
                                                          debuff_mira)

    valor_dificuldade = dificuldades[dificuldade]

    return sistema_tiros(npc, quantidade_tiros, resultado, resultado_final,
                         sist_causar_dano, valor_dificuldade, dic_local_tiros(), local), resultado


def rolagem_dado_causar_dano(npc, pericia_arma, confiabilidade_armar, buff_mira, debuff_mira):
    resultado, falha = rolagem_dados_criticos(npc, confiabilidade_armar)
    return resultado + int(npc.get_reflexo()) + pericia_arma + buff_mira - debuff_mira, resultado


def sistema_tiros(npc, quantidade_tiros, resultado, resultado_final, sist_causar_dano, valor_dificuldade,
                  localTiroDic, local):
    boleano_local_especifico = False
    acertos = 0

    # Se o local não for especificado entao ele o tiro vai ser em um local especifico
    if local != '':
        boleano_local_especifico = True

    # 1 tiro
    if quantidade_tiros == 1:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = 1
            localTiroDic = resultado_tiros_acertados(npc, 1, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    # Rajada de 3 tiros
    elif quantidade_tiros == 3:
        resultado_final += resultado + 3
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = ceil(random(1, 6) / 2)
            localTiroDic = resultado_tiros_acertados(npc, acertos, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    # Rajada de mais de 3 tiros
    elif quantidade_tiros > 3:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = resultado_final - valor_dificuldade

            if acertos > quantidade_tiros:
                acertos = quantidade_tiros

            localTiroDic = resultado_tiros_acertados(npc, acertos, localTiroDic,
                                                     boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    return acertos, localTiroDic, resultado_final
