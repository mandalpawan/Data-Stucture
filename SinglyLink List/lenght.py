class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class singlyLinkList:
    def __init__(self):
        self.head = None
    def appendStart(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur_node = self.head
            newNode = Node(data)
            self.head = newNode
            newNode.next = cur_node

    def appendEnd(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def print_list(self):
        if(self.head== None):
            print("This is a empty list ")
        else:
            temp = self.head
            while(temp != None):
                print(temp.value,end=' ')
                temp = temp.next

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return (count)
        
mylist = singlyLinkList()
mylist.appendEnd(1)
mylist.appendEnd(2)
mylist.appendEnd(3)
mylist.appendEnd(4)
mylist.appendEnd(5)
mylist.print_list()
print()
print(mylist.length())


