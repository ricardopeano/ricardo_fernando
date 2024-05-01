import random

def f(mapa): #Funcao para formatar o mata final, com cores
    import copy
    lista = copy.deepcopy(mapa)
    for l, linha in enumerate (lista):
        for c, letra in enumerate (linha):
            if letra == 'N':
                lista[l][c] = (u"\u001b[42m   \u001b[0m")
            if letra == 'X':
                lista[l][c] = (u"\u001b[41m   \u001b[0m")
            if letra == 'A':
                lista[l][c] = (u"\u001b[44m   \u001b[0m")
            if letra == ' ':
                lista[l][c] = (u"\u001b[30m   \u001b[0m")
    print('   A   B   C   D   E   F   G   H   I   J')
    for i in range (10):
        print(i+1, lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], i+1)
    print('   A   B   C   D   E   F   G   H   I   J')
    return ''

def posicao_suporta(mapa, b, l, c, o):
    if o == 'h':
        if c + b > len(mapa):
            return False
        for i in range(b):
            if mapa[l][c+i] != ' ':
                return False
    if o == 'v':
        if l + b > len(mapa):
            return False
        for i in range(b):
            if mapa[l+i][c] != ' ':
                return False
    return True

def colocando_noMapa(mapa, b, l, c, o):
    tam = len(mapa)
    if o == 'v':
        for i in range(l, l+b):
            mapa[i][c] = 'N'
    elif o == 'h':
        for i in range (c, c+b):
            mapa[l][i] = 'N'
    return mapa

def aloca_navios(mapa, lista):
    tam = len(mapa)
    l = random.randint(0, tam-1)
    c = random.randint(0, tam-1)
    o = random.choice(['h', 'v'])
    for b in lista:
        cabe = posicao_suporta(mapa, b, l, c, o)
        while cabe == False:
            l = random.randint(0, tam-1)
            c = random.randint(0, tam-1)
            o = random.choice(['h', 'v'])
            cabe = posicao_suporta(mapa, b, l, c, o)
        mapa_alocado = colocando_noMapa(mapa, b, l, c, o)
        mapa_final_comp = mapa_alocado
    return mapa_final_comp

def aloca_naviosUser(mapa, b, l, c, o):
    import random
    tam = len(mapa)
    if posicao_suporta(mapa, b, l, c, o) == True:
        if o == 'h':
            for i in range (c, c+b):
                mapa[l][i] = 'N'
        if o == 'v':
            for i in range (l, l+b):
                mapa[i][c] = 'N'
    return mapa

def cria_mapa(N):
    linha = [' ']*N
    matriz=[linha]*N
    return matriz

def foi_derrotado(mapa):
    for l in mapa:
        for c in l:
            if c == 'N':
                return False
    return True

letras_validas = 'abcdefghijABCDEFGHIJ'

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {'cruzador': 1, 'torpedeiro': 2, 'destroyer': 1, 'couracado': 1, 'porta-avioes': 1},
    'França': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Austrália': {'couracado': 1, 'cruzador': 3, 'submarino': 1, 'porta-avioes': 1, 'torpedeiro': 1},
    'Rússia': {'cruzador': 1, 'porta-avioes': 1, 'couracado': 2, 'destroyer': 1, 'submarino': 1},
    'Japão': {'torpedeiro': 2, 'cruzador': 1, 'destroyer': 2, 'couracado': 1, 'submarino': 1}
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

# Escolhe o pais do computador
lista_paises = ['Brasil', 'França', 'Austrália', 'Rússia', 'Japão']
pais_computador = random.choice(lista_paises)

# Prints iniciais
print('Iniciando o Jogo!')
print(f'Computador está alocando os navios de guerra do país {pais_computador}...')
print('Computador já está em posição de batalha!')
print()

# Formatacao lista de paises no terminal
i = 1
for pais, navios in PAISES.items():
    print(f"{i}: {pais}:")
    for navio, qtd in navios.items():
        print(f"   {qtd} {navio}")
    print()
    i += 1

# Escolha pais usuario:
numero_pais = int(input("Qual o número da nação da sua frota? "))
print()
dic_escolhaPais = {1:'Brasil', 2:'França', 3:'Austrália', 4:'Rússia', 5:'Japão'}
pais_usuario = dic_escolhaPais[numero_pais]
# Se a escolha do usuario for igual a do computador:
while pais_usuario == pais_computador:
    print("Você escolheu o mesmo país que o computador. Por favor, escolha outro.")
    print()
    numero_pais = int(input("Qual o número da nação da sua frota? "))
    print()
    dic_escolhaPais = {1:'Brasil', 2:'França', 3:'Austrália', 4:'Rússia', 5:'Japão'}
    pais_usuario = dic_escolhaPais[numero_pais]
    if pais_usuario != pais_computador:
      break


print(f'Você escolheu a nação {pais_usuario}')
print('Agora é a sua vez de alocar seus navios de guerra!')
print()

if pais_usuario == 'Brasil':
    lista_navios = ['cruzador', 'torpedeiro', 'torpedeiro', 'destroyer', 'couracado', 'porta-avioes']
if pais_usuario == 'França':
    lista_navios = ['cruzador', 'cruzador', 'cruzador', 'porta-avioes', 'destroyer', 'submarino', 'couracado']
if pais_usuario == 'Austrália':
    lista_navios = ['couracado', 'cruzador', 'cruzador', 'cruzador', 'submarino', 'porta-avioes', 'torpedeiro']
if pais_usuario == 'Rússia':
    lista_navios = ['cruzador', 'porta-avioes', 'couracado', 'couracado', 'destroyer', 'submarino']
if pais_usuario == 'Japão':
    lista_navios = ['torpedeiro', 'torpedeiro', 'cruzador', 'destroyer', 'destroyer', 'couracado', 'submarino']

# Cria os mapas
matriz_comp = cria_mapa(10)
matriz_user = cria_mapa(10)

print(f'COMPUTADOR - {pais_computador}')
print()
mapa_comp = f(matriz_comp)
print()

print(f'JOGADOR - {pais_usuario}')
print()
mapa_user = f(matriz_user)
print()


navio_pendente = lista_navios[0]

for i in range (len(lista_navios)):
    navio_pendente = lista_navios[i]
    print(f'Alocar: {navio_pendente} ({CONFIGURACAO[navio_pendente]} blocos)')
    print(f'Próximos: {lista_navios[i+1:]}')
    print()
    letra = None
    while True:
        letra = input('Informe a Letra: ')
        if letra == "":
            print('Letra inválida')
        elif letra not in letras_validas:
            print('Letra inválida')
        else:
            break