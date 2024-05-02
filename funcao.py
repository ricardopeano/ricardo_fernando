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
        print(i, lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], i)
    print('   A   B   C   D   E   F   G   H   I   J')
    return ''