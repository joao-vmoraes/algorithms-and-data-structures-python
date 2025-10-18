def quickSort(list , start , end):
    if end is None:
        end = len(list) - 1
    if start < end:
        pivo = partition(list, start, end)
        quickSort(list, start, pivo - 1)
        quickSort(list, pivo + 1, end)

def partition(list, start, end):
    pivo = list[end]
    i = start
    for j in range(start, end):
        if list[j] <= pivo:
            trocar(list, i , j)
            i = i + 1
    trocar(list, end, i)
    return i

def trocar(list, i, j):
    aux = list[i]
    list[i] = list[j]
    list[j] = aux


lista = [3,4,8,4,1,5,9,6,12,3,5,11]
quickSort(lista, 0, None)
print(lista)
