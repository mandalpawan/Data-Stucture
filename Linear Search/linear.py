pos = -1

def search(list,num): 
    for i in range(len(list)):
        global pos
        pos = i
        if(list[i]==num):
            return True
    return False

list = [1,5,8,96,2,5,4,8,56,2,5,8,7,6,9,3,12]
number = int(input("Enter Number want to find = "))

value = search(list,number)
if (value):
    print("Element are found at =",pos+1)
else:
    print("Element are not found")
