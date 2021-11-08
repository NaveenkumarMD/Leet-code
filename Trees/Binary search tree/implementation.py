class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def preorder(self):
        if self:
            
            if self.left:
                self.left.preorder()
            print(str(self.data), end='')
            if self.right:
                self.right.preorder()
        
if __name__=="__main__":
    tree=TreeNode(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(1)
    tree.insert(7)
    tree.insert(9)
    tree.preorder()
    