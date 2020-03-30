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

clist = Circular()
clist.append('B')
clist.append('C')
clist.append('D')
clist.append('E')
clist.prepend('A')
clist.print_list()
