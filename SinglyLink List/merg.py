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
    
    def merge_sorted(self,llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.value <= q.value:
                s=p
                p = s.next
            else:
                s = q
                q = s.next
            new_head =  s

        while p and q:
            if p.value <= q.value:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

                    

mylist1 = singlyLinkList()
mylist2 = singlyLinkList()
mylist1.appendEnd(1)
mylist1.appendEnd(5)
mylist1.appendEnd(7)
mylist1.appendEnd(9)
mylist1.appendEnd(10)

mylist2.appendEnd(2)
mylist2.appendEnd(3)
mylist2.appendEnd(4)
mylist2.appendEnd(6)
mylist2.appendEnd(8)

mylist1.print_list()
print()
mylist2.print_list()
print("After merge  list")
mylist1.merge_sorted(mylist2)
mylist1.print_list()





