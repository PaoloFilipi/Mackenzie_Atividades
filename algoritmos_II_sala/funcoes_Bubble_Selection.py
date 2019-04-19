def BubbleSort(L):
    for i in range(1, len(L)):
        for j in range(0, len(L) - i):
            if L[j] > L[j + 1]:
                aux = L[j]
                L[j] = L[j + 1]
                L[j + 1] = aux
    return L


def SelectionSort(L):
    for i in range(0, len(L)):
        for j in range(i + 1, len(L)):
            if L[j] < L[i]:
                aux = L[j]
                L[j] = L[i]
                L[i] = aux
    return L





L = [50, 30, 40, 20, 10]
print(L)

print(BubbleSort(L))
print(SelectionSort(L))
