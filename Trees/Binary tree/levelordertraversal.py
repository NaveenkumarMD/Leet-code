class Treenode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def levelorder(self,root):
        from collections import deque
        queue=deque()
        temp=root
        queue.append(temp)
        while queue:
            temp=queue.popleft()
            print(temp.data)
            if temp.left:queue.append(temp.left)
            if temp.right:queue.append(temp.right)
    def findmaxlevel(self,root):
        if root is None:
            return 0
        left=self.findmaxlevel(root.left)
        right=self.findmaxlevel(root.right)
        if left>right:
            return left+1
        else:
            return right+1
        

x=Treenode(90)
x.left=Treenode(23)
x.right=Treenode(99)
x.right.left=Treenode(97)

x.levelorder(x)
print(x.findmaxlevel(x))