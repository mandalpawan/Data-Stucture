# Python program for implementation of Bubble Sort 

def bubble_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

ls = [95,45,85,25,6,23,1,2,87,69,12]
bubble_sort(ls)
print(ls)

for i in range(len(ls)):
    print(ls[i])



arr = [64, 34, 25, 12, 22, 11, 90] 

bubble_sort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 
