"Use Stack and Convert Decimal Number To Binary Number"

from Stack import Stack 

def binary_Convertor(number):
    s = Stack()

    while number > 0:
        remainder = number %2
        s.push(remainder)
        number = number //2

    binary_number = ""
    while not s.is_empty():
        binary_number += str(s.pop())
    return binary_number
    
print(binary_Convertor(242))        