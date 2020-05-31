def bubbleSort(array):

    for i in range(len(array)- 1):
        for j in range(len(array) - 1 -i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array    

if __name__ == "__main__":

    print(bubbleSort([1, 5 ,3, 2, 4, 8, 7]))