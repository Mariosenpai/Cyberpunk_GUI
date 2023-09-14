from random import randint as random
from math import ceil


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
  local = random(1,10)

  if local == 1:
    return 'cabeca'
  elif local in [2,3,4]:
    return 'torso'
  elif local == 5:
    return 'braco direito'
  elif local == 6:
    return 'braco esquerdo'
  elif local in [7,8]:
    return 'perna direita'
  else:
    return 'perna esquerda'

def acertoResultado(acertos, localTiroDic):
  for i in range(1,acertos+1):
    #O local é aleatorio quando voce não especifica o mesmo
    local = localCorpo()
    localTiroDic = adiciona_dano_ao_local(localTiroDic, local)
  #Qualquer dano na cabeca é dobrado
  localTiroDic['cabeca'] *= 2
  print(localTiroDic)

def acertoResultadoLocalEspecifico(acertos, localTiroDic, local):
  for i in range(1,acertos+1):
    localTiroDic = adiciona_dano_ao_local(localTiroDic,local)

  #Qualquer dano na cabeca é dobrado
  localTiroDic['cabeca'] *= 2
  print(localTiroDic)

def calcula_dano():
  dano = 0
  for i in range(dado_de_mult):
    dano += random(1,dado_de_dano)

  if (dano-valor_de_subtracao) <= 0 :
    return 1
  else:
    return dano - valor_de_subtracao

def adiciona_dano_ao_local(localTiroDic, local):

  dano = calcula_dano()
  if local in localTiroDic:
    localTiroDic[local] += dano
  else:
    localTiroDic[local] = dano
  return localTiroDic

def escolhe_local(id_local):

  local = ['cabeca','torso','braco direito','braco esquerdo','perna direita','perna esquerda']

  return local[id_local - 1]

def resultado_tiros_acertados(acertos, localTiroDic, boleano_local_especifico = False, local = ''):
  if not boleano_local_especifico :
    acertoResultado(acertos, localTiroDic)
  else:
    acertoResultadoLocalEspecifico(acertos,localTiroDic,local)

def armar_falhou():
  evitar_falha = random(1,10)
  if confiabilidade == 1:
    if evitar_falha <= 8 :
      print("Armar falhou")
      return True
  if confiabilidade == 2:
    if evitar_falha <= 5:
      print("Armar falhou")
      return True
  if confiabilidade <= 3:
      print("Armar falhou")
      return True

def tipos_falha_criticas():
  tipo_falha_critica = random(1,10)

  if tipo_falha_critica <= 4:
    print("Nada acontece...")
    return False
  elif tipo_falha_critica == 5 :
    print("Voce deixa sua arma cair")
    return True
  elif tipo_falha_critica == 6 :
    print("Atinge algo inofencivo sem ser o alvo")
    return True
  elif tipo_falha_critica == 7 :
    print("Arma trava")
    return True
  elif tipo_falha_critica == 8 :
    print("Voce se atira na/o", localCorpo())
    print(f"Levou {calcula_dano()} de dano no local")
    return True
  elif tipo_falha_critica >= 9 :
    print("Voce atinge um membro do grupo")
    print("Todo o dano a parte de agora em diante será direicionado para um membro de o grupo")
    return False

def rolagem_dados_criticos():

  resultado_dado = random(1,10)
  falha = False
  print("\n******************************")
  print("* Resultado do dado =", resultado_dado ,"     *")
  print("******************************\n")
  if resultado_dado == 10:
    print("******************************")
    print("ACERTO CRITICO!! \nrolagem de dado adicional")
    nova_rolagem = random(1,10)
    print("Resultado da nova rolagem =", nova_rolagem )
    resultado_dado += nova_rolagem
    print("Resultado final do dado =", resultado_dado)
    print("******************************")
  elif resultado_dado == 1:
    print("******************************")
    print("FALHA CRITICA!!")
    if arma_automatica == 1:
      falha = armar_falhou()
    elif arma_automatica == 2:
      falha = tipos_falha_criticas()
    print("******************************")

  return resultado_dado, falha

def mira_buff_debuff():

  boleano_local_especifico = False
  debuff_local_especifico = 0
  buff_mira = 0
  local = ''

  if mira == 1:
    print("Voce mirou em um local especifico?")
    local_especifico = int(input("Sim (1) ou Nao (2) :"))

    if local_especifico == 1 :
      debuff_local_especifico = 4
      print("Qual foi o local que voce mirou ?")
      print("1 - cabeca\n2 - torso\n3 - braco direita\n4 - braco esquerdo\n5 - perna direita \n6 - perna esquerda")
      local_mirado = int(input("Escolha:"))
      local = escolhe_local(local_mirado)
      boleano_local_especifico = True

    elif local_especifico == 2:
      turnos_mirando = int(input("Esta mirando por turnos tempo:"))

      if turnos_mirando <= 3:
        buff_mira = turnos_mirando
      else:
        buff_mira = 3

  return buff_mira, debuff_local_especifico, boleano_local_especifico ,local