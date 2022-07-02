class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root.data<data:
            if self.root.right:
                self.root.right.insert(data)
            else:
                self.root.right=Node(data)
        else:
            if self.root.left:
                self.left.insert(data)
            else:
                self.root.left=Node(data)
    def preorder(self,root):
        print(root)
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
x=BinaryTree()
x.insert(6)
x.insert(3)
x.preorder(x.root)