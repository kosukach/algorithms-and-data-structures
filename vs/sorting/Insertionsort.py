def insertionSort(array):

    for i in range(len(array)):
        j = i
        while array[j-1] > array[j] and j>0:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                j = j - 1 
    return array


if __name__ == "__main__":
    print(insertionSort([100, 4, 5, 5, 2, 32, 4 ,23,1]))