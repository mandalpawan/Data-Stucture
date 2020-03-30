class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Circular:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node


    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            cur = self.head
            while(cur.next != self.head):
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def print_list(self):
        cur = self.head
        while cur :
            print(cur.value)
            cur = cur.next
            if(cur == self.head):
                break

    def remove_node(self,key):
        if self.head.value == key:
            cur_node = self.head
            nxt = cur_node.next
            while(cur_node.next != self.head):
                cur_node = cur_node.next
            cur_node.next = nxt
            self.head = nxt
        else:
            cur_node = self.head
            pre = None
            while(cur_node.next != self.head):
                pre = cur_node
                cur_node = cur_node.next
                if(cur_node.value == key):
                    pre.next = cur_node.next
                    cur_node= cur_node.next

    def __len__(self):
        index = 0
     
        cur = self.head
        while cur:
            index += 1
            cur = cur.next
            if (cur == self.head):
                break
        return index

    def split(self):
        size = len(self)
        
        if size == 0:
            return None
        if size ==1:
            return self.head
        
        mid = size//2
        count = 0

        pre = None
        cur = self.head

        while cur and count < mid:
            count +=1
            pre = cur
            cur = cur.next
        pre.next = self.head

        split_list = Circular()
        while cur.next != self.head:
            split_list.append(cur.value)
            cur = cur.next
        split_list.append(cur.value)

        self.print_list()
        print("-------------------")
        split_list.print_list()

                

clist = Circular()
clist.append('B')
clist.append('C')
clist.append('D')
clist.append('E')
clist.prepend('A')
#clist.remove_node('B')
#clist.remove_node('E')
#print(clist.length())
#clist.print_list()
clist.split()
