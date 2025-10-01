def MergeSort(list, start=0 , end = None):
    if end is None:
        end = len(list)

    if (end - start > 1):
        mid = ( end + start ) // 2
        MergeSort(list , start , mid)
        MergeSort(list , mid, end)
        merge(list , start , mid, end)

def merge(list , start , mid , end):
    n1 = mid - start 
    n2 = end - mid

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = list[start + i]
    for i in range(n2):
        right[i] = list[mid + i]

    i, j = 0 , 0
    for k in range(start, end):

        if i >= len(left):
            list[k] = right[j]
            j = j + 1
        elif j >= len(right):
            list[k] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            list[k] = left[i]
            i = i + 1
        else:
            list[k] = right[j]
            j = j + 1



array = [ 34, 71, 22, 3 ,4 ,5 ,6 ,1 ,4 ,32 ,2 ,9 , 81 , 25 , 19 , 11 , 20]
MergeSort(array)
print(array)