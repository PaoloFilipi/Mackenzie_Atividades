def exibirVelha(matriz):
    for l in range(3):
        for c in range(3):
            print(f'\033[32m[{matriz[l][c]:^5}]',end='')
        print()

def verificaGanhador(matriz):
    cont_DiagoPx = 0
    cont_DiagoPo = 0
    cont_DiagoSx = 0
    cont_DiagoSo = 0

    for l in range(3):
        for c in range(3):
            if(l == c ):
               if((matriz[l][c]).upper() == "X"):
                   cont_DiagoPx += 1
               if ((matriz[l][c]).upper() == "O"):
                   cont_DiagoPo += 1
            if (l + c == 2):
                if ((matriz[l][c]).upper() == "X"):
                    cont_DiagoSx += 1
                if ((matriz[l][c]).upper() == "O"):
                    cont_DiagoSo += 1
    if(cont_DiagoPx == 3):
        print('Jogador 1 ganhou')
        print()
        exibirVelha(matriz)
        return False
    if (cont_DiagoPo == 3):
        print('Jogador 2 ganhou')
        print()
        exibirVelha(matriz)
        return False
    if (cont_DiagoSx == 3):
        print('Jogador 1 ganhou')
        print()
        exibirVelha(matriz)
        return False
    if (cont_DiagoSo == 3):
        print('Jogador 2 ganhou')
        print()
        exibirVelha(matriz)
        return False
    for i in range(3):
        if matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2]:
            if(matriz[i][0].upper() == "X"):
                print('Jogador 1 ganhou')
                exibirVelha(matriz)
                return False
            if (matriz[i][0].upper() == "O"):
                print('Jogador 2 ganhou')
                exibirVelha(matriz)
                return False
        elif matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i]:

            if (matriz[0][i].upper() == "X"):
                print('Jogador 1 ganhou')
                exibirVelha(matriz)
                return False
            if (matriz[0][i].upper() == "O"):
                print('Jogador 2 ganhou')
                exibirVelha(matriz)
                return False

def verificaPosição(matriz,l,c):

    if(matriz[l][c].upper() == "X" or matriz[l][c].upper() == "O" ):
        print("Deu ruim")
        return True
    else:
        return False

def jogodaVelha():
    print('-=-=-=-=-=-=-=-=-=-=-=-= Jogo da Velha -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    print('\033[33m Regra do jogo: ')
    print('\t \033[32m Simbolo do jogador 1 :\33[31m x ')
    print('\t \033[32m Simbolo do jogador 2 :\33[35m o ')

    matrizVelha = [['B','B','B'],['B','B','B'],['B','B','B']]
    cont = 0
    status = True

    while(cont < 9 and status == True):
        cont += 1
        if((cont % 2) == 1):
            linha = int(input('\33[31m Jogador 1 digite o numero da linha que deseja preencher: '))
            coluna = int(input('\33[31m Jogador 1 digite o numero da coluna que deseja preencher: '))
            if (verificaPosição(matrizVelha, linha, coluna)== True):
                print("FAlseee")
                while (verificaPosição(matrizVelha, linha, coluna) == True):
                    print("Posição já preenchida,escolha outra!!")
                    print()
                    linha = int(input('\33[31m Jogador 1 digite o numero da linha que deseja preencher: '))
                    coluna = int(input('\33[31m Jogador 1 digite o numero da coluna que deseja preencher: '))
                    escolha = str(input('\33[31m Preencha com o simbolo: '))
            escolha = str(input('\33[31m Preencha com o simbolo: '))
            verificaPosição(matrizVelha, linha, coluna)


            while escolha.upper() != "X" :
                escolha = str(input('\33[31m Preencha com o simbolo certo: '))
            matrizVelha[(linha-1)][(coluna-1)] = escolha

            exibirVelha(matrizVelha)

        if ((cont % 2) == 0):
            linha = int(input('\33[35m Jogador 2 digite o numero da linha que deseja preencher: '))
            coluna = int(input('\33[35m Jogador 2 digite o numero da coluna que deseja preencher: '))
            if (verificaPosição(matrizVelha, linha, coluna) == True):
                print("FALSEEEEE")
                while (verificaPosição(matrizVelha, linha, coluna) == True):
                    print("Posição já preenchida,escolha outra!!")
                    print()
                    linha = int(input('\33[31m Jogador 1 digite o numero da linha que deseja preencher: '))
                    coluna = int(input('\33[31m Jogador 1 digite o numero da coluna que deseja preencher: '))
            escolha = str(input('\033[35m Preencha com o simbolo: '))

            while escolha.upper() != 'O':
                escolha = str(input('\033[35m Preencha com o simbolo certo: '))
            matrizVelha[(linha - 1)][(coluna - 1)] = escolha
            exibirVelha(matrizVelha)
        verificaGanhador(matrizVelha)
        if(verificaGanhador(matrizVelha)== False):
            status = False

    print("Deu Velha!")
jogodaVelha()
