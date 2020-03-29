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
    def deleteFirst(self):
        if self.head is None:
            print("There is no element for deleting")
        else:
            cur_node = self.head
            self.head = cur_node.next
            cur_node.next = None   
    def deleteLast(self):
        if self.head.next is None:
            self.deleteFirst()
        else:
            cur_node = self.head
            pre = None
            while cur_node.next:
                pre = cur_node
                cur_node = cur_node.next
            pre.next = None 
            
    def print_list(self):
        if(self.head== None):
            print("This is a empty list ")
        else:
            temp = self.head
            while(temp != None):
                print(temp.value,end=' ')
                temp = temp.next
    def reverse(self):
        if self.head.next is None:
            self.head = self.head
        else:
            pre = None
            cur_node = self.head
            while cur_node:
                nxt = cur_node.next
                cur_node.next = pre
                pre = cur_node
                cur_node = nxt
            self.head = pre
    def rotate(self,key):
        cur_node = self.head
        p = None
        q = None
        while cur_node.next:
            if cur_node.value == key:
                p = cur_node
                nxt = cur_node.next
            cur_node = cur_node.next
        q = cur_node
        q.next = self.head
        p.next = None
        self.head = nxt

    def removeDublicate(self):
        cur= self.head
        prev = None
        dup_value = dict()
        while cur:
            if cur.value in dup_value:
                prev.next = cur.next
            else:
                dup_value[cur.value] = 1
                prev = cur
            cur = prev.next

    def count_occur(self,data):
        count =0
        cur = self.head
        while cur:
            if cur.value == data:
                count +=1
            cur = cur.next
        return count
    
    def count_recursive(self,node,data):
        if not node:
            return 0
        if node.value == data:
            return 1+ self.count_recursive(node.next,data)
        else:
            return  self.count_recursive(node.next,data)
    
    def sec_lst_ele(self):
        cur = self.head
        pre = None
        sec = None
        while cur.next:
            pre = cur
            sec = pre.value
            cur = cur.next
        return sec

mylist = singlyLinkList()
mylist.appendEnd(1)
mylist.appendEnd(2)
mylist.appendEnd(3)
mylist.appendEnd(4)
mylist.appendEnd(5)
mylist.appendEnd(6)
mylist.appendEnd(1)
mylist.print_list()
print()
#print(mylist.count_occur(1))
print(mylist.sec_lst_ele())






