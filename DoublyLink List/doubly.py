class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class DoblyLinkList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = None
            newNode.prev = None
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = newNode
            newNode.prev = cur_node
            newNode.next = None

    def prepend(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = None
            newNode.prev = None
        else:
            cur_node = self.head
            cur_node.prev = newNode
            newNode.next = cur_node
            newNode.prev = None
            self.head = newNode

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next 
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
            cur = cur.next

  
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


dllist = DoblyLinkList()
dllist.append(2)
dllist.append(3)
dllist.append(5)
dllist.prepend(1)
dllist.add_after_node(3,4)
dllist.add_before_node(5,4.4)
dllist.print_list()

