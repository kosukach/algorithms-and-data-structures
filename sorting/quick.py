def quickSort(array, low, high):

    if low >= high:
        return 

    pivotIndex = partition(array, low, high)
    quickSort(array, low, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, high)

    return array


def partition(array, low, high):

    pivot = (high+low)//2
    swap(array, pivot, high)

    i = low

    for j in range(low, high):
        if array[j] <= array[high]:
            swap(array, j, i)
            i = i + 1
    swap(array, i, high)
    return i




def swap(array, index1, index2):

    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

if __name__ == "__main__":
    from timeit import Timer
    array = [1, 123, 123, 111, 4, 54, 763, 1, 9, 9 ,-1 ,12, -312]
    t = Timer("quickSort(array, 0, len(array) - 1)", "from __main__ import quickSort, array")
    
    print(t.timeit(number = 10000))



