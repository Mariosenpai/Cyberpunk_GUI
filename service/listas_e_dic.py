def locais_corpo():
    return ["Cabeça", "Torso", "Braço direito", "Braço esquerdo", "Perna direita", "Perna esquerda"]


def atributos():
    return ['inteligencia', 'reflexo', 'tecnologia', 'auto controle', 'atratividade', 'sorte', 'movimento',
            'tipo corporal', 'empatia']


def classes():
    return ["solo", "midia", "nomade", "trilha rede", "corporativo", "medicanico", "atravessador"]


def tipos_arma():
    return ["Pistola", "Submetralhadora", "Fuzil", "Espingarda", "Arma pesada", "Exotica", "Arma Branca",
            "Maos vazia"]


# dicionario de todos os membros do corpo e seu dano causada a cada um deles
def dic_local_tiros():
    return {'Cabeça': 0, 'Torso': 0, 'Braço direito': 0, 'Braço esquerdo': 0, 'Perna direita': 0,
            'Perna esquerda': 0, }


def dic_tipo_corporal_dano():
    return {'Muito Fraco': -2, 'Fraco': -1, 'Medio': 0, 'Forte': 1, 'Muito Forte': 2}


# Separa por um \n
def lista_armas_brancas():
    with open(f"dados/armas/armas_brancas.txt", 'r', encoding='utf8') as arquivo_aberto:
        return arquivo_aberto.read().split('\n')


def lista_armas_de_fogo():
    with open(f"dados/armas/armas_de_fogo.txt", 'r', encoding='utf8') as arquivo_aberto:
        return arquivo_aberto.read().split('\n')


def lista_ciberware_opticos():
    with open(f"dados/cyberwares/cyberopticos.txt", 'r', encoding='utf8') as arquivo_aberto:
        return arquivo_aberto.read().split('\n')


def lista_ciberware_neurais():
    with open(f"dados/cyberwares/ciberneural.txt", 'r', encoding='utf8') as arquivo_aberto:
        return arquivo_aberto.read().split('\n')


def lista_ciberware_audio():
    with open(f"dados/cyberwares/ciberaudio.txt", 'r', encoding='utf8') as arquivo_aberto:
        return arquivo_aberto.read().split('\n')
