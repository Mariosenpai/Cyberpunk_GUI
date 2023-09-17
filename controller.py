from service import *

falha = False
print("*********************************************")
quantidade_tiros = int(input("Quantidade de tiros:"))
print("******** DIFICULDADE ********" +
      "\n1 - Queima roupa - 10"
      "\n2 - Curta distancia - 15\n3 - Media distancia - 20\n4 - Longa distancia - 25\n5 - Extrema distancia - 30")
dificuldade = int(input("Dificuldade:"))

# Mira
print("******* MIRA *******")
print("Voce mirou?")
mira = int(input("Sim (1) ou Nao (2) :"))

# Buff e debuff para a ação de mira

buff_mira, debuff_local_especifico, boleano_local_especifico, local = mira_buff_debuff()

print("\nBUFF na precisao =", buff_mira)
print("DEBUFF na precisao = -", debuff_local_especifico)

# Mira


dd = pegaDificuldade(dificuldade)

# Rolagem de dados englobando as possibilidades de acertos e falhas critas
resultado_dado, falha = rolagem_dados_criticos()

if not falha:

    print("****** RESULTADO DA ACAO ******")

    resultado = REF + pericia + resultado_dado + buff_mira - debuff_local_especifico

    localTiroDic = {'cabeca': 0, 'torso': 0, 'braco direito': 0, 'braco esquerdo': 0, 'perna direita': 0,
                    'perna esquerda': 0, }

    if quantidade_tiros == 1:
        print("resultado =", resultado)
        if dd <= resultado:
            resultado_tiros_acertados(1, localTiroDic,
                                      boleano_local_especifico, local_corpo_aleatorio())
        else:
            print("Errou o tiro!!")

    elif quantidade_tiros == 3:

        resultado = resultado + 3
        print("resultado =", resultado)
        if dd <= resultado:

            acertos = ceil(random(1, 6) / 2)
            print("Acertos =", acertos)
            resultado_tiros_acertados(acertos, localTiroDic,
                                      boleano_local_especifico, local)

        else:
            print("Errou todos os tiros!!")

    elif quantidade_tiros > 3:

        print("resultado =", resultado)
        if dd < resultado:

            acertos = resultado - dd

            # Se o resultado menos a dificuldade der um valor maior que a quantidade,
            # a quantidade de acertos vai ser igual a quantidade de tiros
            if acertos > quantidade_tiros:
                acertos = quantidade_tiros

            print(f"Acertou {acertos} tiros!")
            resultado_tiros_acertados(acertos, localTiroDic,
                                      boleano_local_especifico, local)

        else:
            print("Errou todos os tir1os!!")
