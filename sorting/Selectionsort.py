def selectionSort(array):

    for i in range(len(array) - 1):
        temp = i
        for j in range(i + 1, len(array)):
            if array[j] < array[temp]:
                temp = j
        if i != temp:
            tempVal = array[temp]
            array[temp] = array[i]
            array[i] = tempVal
    return array      
if __name__ == "__main__":

    print(selectionSort([2, 3, 4, 5, 6, 1]))