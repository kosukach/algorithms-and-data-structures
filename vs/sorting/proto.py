def proto(array):
    if len(array) == 1:
        return array
    average = 0
    for item in array:
        average = average + item

    average = average/len(array)
    little = []
    big = []

    for item in array:
        if item > average:
            big.append(item)
        else:
            little.append(item)
        
    little = proto(little)
    
    big = proto(big)
    
    return little + big
if __name__ == "__main__":

    print(proto([1 ,3, 5, 7, 8, 2]))