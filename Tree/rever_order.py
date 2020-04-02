class Stack(object):
    def __init__(self):
        self.item = []

    def push(self,data):
        return self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
    
    def is_empty(self):
        return len(self.item) ==0

    def peek(self):
        if not self.is_empty():
            return self.item[-1]
    
    def size(self):
        return len(self.item)

    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "reverselevelorder_print":
            return self.reverselevelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False


    def reverselevelorder_print(self, start):
        stack = Stack()
        queue = Queue()
        queue.enqueue(start)
        index= 1
        while len(queue)>0:
            node = queue.dequeue()

            stack.push(node)
            if node.left:
                index+=1
                queue.enqueue(node.left)
            if node.right:
                index+=1
                queue.enqueue(node.right)
        trasversal = ''
        while len(stack)>0:
            node = stack.pop()
            trasversal += str(node.value)
        print('No. of Root of tree',index)
        return trasversal



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("reverselevelorder_print"))