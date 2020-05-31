
def mergeSort(nums):
    
	if len(nums) == 1:                                  
		return
		
	middle_index = len(nums) // 2
		
	left_half = nums[:middle_index]
	right_half = nums[middle_index:]
	
	mergeSort(left_half)
	mergeSort(right_half)
	
	i = 0
	j = 0
	k = 0
	
	while i<len(left_half) and j<len(right_half):
		if left_half[i] < right_half[j]:
			nums[k] = left_half[i]
			i = i + 1
		else:
			nums[k] = right_half[j]
			j = j + 1
			
		k = k + 1
		
	while i<len(left_half):
		nums[k] = left_half[i]
		k = k + 1
		i = i + 1		
	
if __name__ == "__main__":
   
	from timeit import Timer
	t = Timer("mergeSort([1, 2, 0, -1, 12, -10, 13, 12])", "from __main__ import mergeSort")
    
	print(t.timeit(number = 100000))