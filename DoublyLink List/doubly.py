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
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


dllist = DoblyLinkList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.print_list()

