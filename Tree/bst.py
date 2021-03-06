class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data >cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("Value is already present in tree")

    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        else :
            return False

    def _find(self,data,cur_node):
        if data>cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left :
            return self._find(data,cur_node.left)
        if data == cur_node.data:
            return True

    def inorder(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._inorder(self.root)
    
    def minValue(self,node):
        cur_node = node
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node
    
    def remove(self,key):
        if self.root:
            self._remove(self.root,key)

    def _remove(self,cur_node,key):
        node = cur_node
        if node is None:
            return False
        if key< node.data:
            node.left = self._remove(node.left,key)
        elif(key>node.data):
            node.right = self._remove(node.right,key)
        else:
            if node.left is None:
                temp = cur_node.right
                root = None
                return temp
            elif node.right is None:
                temp = cur_node.left
                root = None
                return temp
            temp = self.minValue(node.right)
            node.data = temp.data
            node.right = self._remove(node.right,temp.data)
        return node

    def _inorder(self,cur_node):
        if cur_node:
            self._inorder(cur_node.left)
            print(str(cur_node.data),end=" - ")
            self._inorder(cur_node.right)


bst = BinaryTree()
bst.insert(15)
bst.insert(5)
bst.insert(8)
bst.insert(6)
bst.insert(24)
bst.insert(19)
bst.insert(30)
bst.insert(21)
bst.inorder()
bst.remove(15)
print("after delete")
bst.inorder()



        

     
