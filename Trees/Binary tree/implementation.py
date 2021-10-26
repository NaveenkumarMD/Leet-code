class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self) -> None:
        self.root=None
    def preorder(self,root):
        temp=root
        if temp:
            print(temp.data)
            self.preorder(temp.left)
            self.preorder(temp.right)
    def postorder(self,root):
        temp=root
        if temp:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data)
    def inorder(self,root):
        temp=root
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
    def insert(self,data):
        temp=self.root
        if temp is None:
            return Node(data)
        else:
            if data<temp.data:
                temp.left=self.insert(data)
            else:
                temp.right=self.insert(data)
        

        
tree=Tree()
tree.root=Node(10)
tree.root.left=Node(7)
tree.root.right=Node(12)
# tree.preorder(tree.root)
# tree.inorder(tree.root)
# tree.postorder(tree.root)
tree.insert(45)


    