#exercicio 4
def diferenciaVet(vet_A, vet_B):
    status = True
    i = 0
    j = 0
    cont_B = len(vet_B)
    cont_A = len(vet_A)

    for i in range(len(vet_A)):
        for j in range(len(vet_B)):
            if (vet_B[j] == vet_A[i]):
                status = True
                cont_B += 1
            else:
                status = False
                cont_B += 1
        if (status == False):
            print('{}'.format(vet_A[i]), end='')

        cont_A += 1

vet_A = [7, 2, 5, 8, 4]

vet_B = [4, 2, 9, 5]

diferenciaVet(vet_A, vet_B)



'''
#exercicio 2
def inverteVetor(vetor_a):

   aux = len(vetor_a)

   for i in range(len(vetor_a)):
        vetor_a[i] = vetor_a[aux]
        if(i > 0 ):
            vetor_a[i] = vetor_a[aux - i]
   print(vetor_a)

vet = [4,9,10,8,6]

inverteVetor(vet)
'''