def insertion_sort(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			
     
num = [22,15,10,77,85,45,63,8,13]
#num =[2,6,4,3]
insertion_sort(num)
print(num)
