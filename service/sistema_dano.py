from .service import *
from .listas_e_dic import *


def sistema_arma_branco():
    pass


def sistema_dano_fisico(npc):
    modicador_dano = dic_tipo_corporal_dano()[npc.modificador_tipo_corporal()]


# Botao para rola os dados
def botao_rolar_dados(sist_causar_dano, npc, arma, pericia_arma, dificuldades, dificuldade, local,
                      buff_mira, debuff_mira, quantidade_tiros=0, rd=0, pd=0):
    confiabilidade_armar = False

    #
    # if npc.confiabilidade != "Não é uma arma automatica":
    #     confiabilidade_armar = True
    resultado_final, resultado = rolagem_dado_causar_dano(npc, pericia_arma, confiabilidade_armar, buff_mira,
                                                          debuff_mira)

    if arma.get_tipo() == 'Arma Branca':
        acertos = 1
        # Resultado final se refere a soma de todos os atributos e resultado se refere a o resultado do dado 1d10
        localTiroDic, resultado_final, resultado = sistema_ataque_fisico(sist_causar_dano, arma, dic_local_tiros(),
                                                                          local, npc, pericia_arma, rd, pd)
    else:
        valor_dificuldade = dificuldades[dificuldade]

        acertos, localTiroDic, resultado_final = sistema_tiros(arma, quantidade_tiros, resultado, resultado_final,
                                                               sist_causar_dano, valor_dificuldade, dic_local_tiros(),
                                                               local)

    return acertos, localTiroDic, resultado_final, resultado


def rolagem_dado_causar_dano(npc, pericia_arma, confiabilidade_armar, buff_mira, debuff_mira):
    resultado, falha = rolagem_dados_criticos(npc, confiabilidade_armar)
    return resultado + int(npc.get_reflexo()) + pericia_arma + buff_mira - debuff_mira, resultado


def PA_arma(arma, resultado_final):

    pa1 = str(arma.get_PA())[0]

    # Verificar se o primeira simbolo é um sinal
    if pa1 in ['-','+']:
        pa2 = arma.get_PA()[1]
        if pa1 == '-':
            return resultado_final - pa2
        elif pa1 == '+':
            return resultado_final + pa2
    else:
        return resultado_final
def sistema_ataque_fisico(sist_causar_dano, arma, localTiroDic, local, npc, pericia_arma, rd, pd):

    dado = random(1, 10)
    dado_inimigo =  random(1, 10)

    resultado = npc.get_reflexo() + pericia_arma + dado

    resultado_inimigo = rd + pd + dado_inimigo

    # Mostra o resultado da rolagem do inimigo
    sist_causar_dano.caption(f"Rolagem dado inimigo = {dado_inimigo}")
    sist_causar_dano.caption(f'Total = {resultado_inimigo}')

    if resultado >= resultado_inimigo:
        sist_causar_dano.success("Voce acertou!!")
        localTiroDic = resultado_tiros_acertados(arma, 1, localTiroDic, True, local)
    else:
        sist_causar_dano.error("Voce errou")

    return localTiroDic, resultado, dado


def sistema_tiros(arma, quantidade_tiros, resultado, resultado_final, sist_causar_dano, valor_dificuldade,
                  localTiroDic, local):
    boleano_local_especifico = False
    acertos = 0

    # as armas podem aumentar ou diminuir a precisão
    resultado_final = PA_arma(arma,resultado_final)

    # Se o local não for especificado entao ele o tiro vai ser em um local especifico
    if local != '':
        boleano_local_especifico = True

    # 1 tiro
    if quantidade_tiros == 1:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = 1
            localTiroDic = resultado_tiros_acertados(arma, 1, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    # Rajada de 3 tiros
    elif quantidade_tiros == 3:
        resultado_final += resultado + 3
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = ceil(random(1, 6) / 2)
            localTiroDic = resultado_tiros_acertados(arma, acertos, localTiroDic, boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")
    # Rajada de mais de 3 tiros
    elif quantidade_tiros > 3:
        if resultado_final >= valor_dificuldade:
            sist_causar_dano.success("Voce acertou!!")
            acertos = resultado_final - valor_dificuldade

            if acertos > quantidade_tiros:
                acertos = quantidade_tiros

            localTiroDic = resultado_tiros_acertados(arma, acertos, localTiroDic,
                                                     boleano_local_especifico, local)
        else:
            sist_causar_dano.error("Voce errou")

    return acertos, localTiroDic, resultado_final
