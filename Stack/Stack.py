'''
Stack In Data Stucture
'''

class Stack:
    def __init__(self):
        self.item = []
        
    "PUSH method is use for insert element in TOP of the STACK"
    def push(self,item):
        self.item.append(item)
    
    "POP method is use to remove element from top of the stack"
    def pop(self):
        return self.item.pop()

    "Print the Stack elemnt"
    def get_stack(self):
        return self.item

    "Check for Stack is empty or not"
    def is_empty(self):
        return self.item == []

    "Check top element of the Stack"
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return "Stack is Empty"

    "Check for length of the stack"
    def length(self):
        return len(self.item)
    

s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.get_stack())
print(s.is_empty())
print(s.peek())
print(s.length())