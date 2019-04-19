def maiorValor(matriz):
    aux = 0
    for l in range(quantLinha):
        for c in range(quantColuna):
            if(matriz[l][c] >= aux):
                aux = matriz[l][c]
    print('-='*30)
    print('O maior valor dessa matriz é: {}'.format(aux))
quantLinha = int(input('Digite a quantidade de linha: '))
quantColuna = int(input('Digite a quantidade e coluna: '))

matriz = []

for l in range(quantLinha):
    linha = []
    for c in range(quantColuna):
        numero = int(input(f'Digite o valor da posição [{l}{c}]: '))
        linha.append(numero)
    matriz.append(linha)
print('-='*30)

for l in range(quantLinha):
    for c in range(quantColuna):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
maiorValor(matriz)