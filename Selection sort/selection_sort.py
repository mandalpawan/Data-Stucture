# Python program for implementation of Selection 
# Sort 


def selection_sort(A):
# Traverse through all array elements 
    for i in range(len(A)): 
        # Find the minimum element in remaining 
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element		 
        A[min_idx], A[i] = A[i], A[min_idx] 

# Driver code to test above 
A = [64, 25, 12, 22, 11] 
selection_sort(A)
print(A)


print ("Sorted array") 
for i in range(len(A)): 
	print(A[i])
