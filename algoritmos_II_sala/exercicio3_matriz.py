def diagonalPrin(matriz):
    soma = 0
    for l in range(0,quantLinha):

        for c in range(0,quantLinha):
            if (l == c):
                print(f'[{matriz[l][c]:^5}]', end='')
                soma += matriz[l][c]
    print()
    print('A soma da diagonal principal é: {}'.format(soma))

quantLinha = int(input('Digite a quantidade de linha e coluna da sua matriz quadrada: '))

matriz = []

for l in range(quantLinha):
    linha = []
    for c in range(quantLinha):
        numero = int(input(f'Digite o valor da posição[{l}{c}]'))
        linha.append(numero)
    matriz.append(linha)
print('-='*30)
for l in range(quantLinha):
    for c in range(quantLinha):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
diagonalPrin(matriz)