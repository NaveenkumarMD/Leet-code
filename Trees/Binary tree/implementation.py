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

tree.insert(45)
tree.preorder(tree.root)


    