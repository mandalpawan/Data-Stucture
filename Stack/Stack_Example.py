"""
Use a stack to check whether or not a string
has balanced usage of parenthesis

Example:
        (),()(),(({[]})) <- Balanced
        ((),{{{)}] ,  [][]]]

        Balanced Example :  {[]}
        Non-Balance Example : (()
        Non-Balance Example : ))
"""
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


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("(((({}))))"))

print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))