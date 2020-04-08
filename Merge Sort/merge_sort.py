#Method 1
# Python program for implementation of MergeSort 
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 



#Method 2
def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i]  <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1 

    result += left[i:]
    result += right[j:]
    return result


def mergeSort2(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst)//2
        left =  mergeSort2(lst[:mid])
        right =  mergeSort2(lst[mid:])
        return merge(left,right)


# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11,13, 5, 6, 7] 
	print ("Given array is", end="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 


arr1 = [12, 11, 13, 5, 6, 7]
print(mergeSort2(arr1))

