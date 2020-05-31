def mergeSort(array):
    if len(array) == 1:
        return array
    array1 = mergeSort(array[0: len(array)//2])
    array2 = mergeSort(array[len(array)//2:len(array)])

    return merge(array1, array2)

def merge(a1, a2):

    output = []
    while a1 and a2:
        if a1[0] < a2[0]:
            output.append(a1[0])
            del a1[0]
        else:
            output.append(a2[0])
            del a2[0]


    for i in range(len(a1)):
        output.append(a1[i])

    for i in range(len(a2)):
        output.append(a2[i])


    return output

if __name__ == "__main__":
    from timeit import Timer
    t = Timer("mergeSort([1, 2, 0, -1, 12, -10, 13, 12])", "from __main__ import mergeSort")
    print(t.timeit(number = 100000))