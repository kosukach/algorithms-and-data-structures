def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    lil = []
    big = []
    for i in range(1, len(array)):
        if array[i] > pivot:
            big.append(array[i])
        else:
            lil.append(array[i])

    return quickSort(lil) + [pivot] + quickSort(big)



if __name__ == "__main__":
    from timeit import Timer
    array = [1, 123, 123, 111, 4, 54, 763, 1, 9, 9 ,-1 ,12, -312]
    t = Timer("quickSort(array)", "from __main__ import quickSort, array")
        
    print(t.timeit(number = 10000))
