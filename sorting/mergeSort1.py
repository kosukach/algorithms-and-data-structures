def mergeSort(array):
    if len(array) == 1:
        return array
    array1 = mergeSort(array[0: len(array)//2])
    array2 = mergeSort(array[len(array)//2:len(array)])

    return merge(array1, array2)

def merge(ai, aj):
    output = []
    i = 0
    j = 0
    while i < len(ai) and j < len(aj):
        if ai[i] < aj[j]:
            output.append(ai[i])
            i = i + 1
        else:
            output.append(aj[j])
            j = j + 1

    while j < len(aj):
        output.append(aj[j])
        j = j + 1

    while i < len(ai):
        output.append(ai[i])
        i = i + 1

    return output

if __name__ == "__main__":
    from timeit import Timer
    t = Timer("mergeSort([1, 2, 0, -1, 12, -10, 13, 12])", "from __main__ import mergeSort")
    print(t.timeit(number = 100000))