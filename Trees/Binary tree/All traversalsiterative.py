class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None
    def addNode(self,data):
        if self.data<data:
            if self.right:
                self.right.addNode(data)
            else:
                self.right=TreeNode(data)
        else:
            if self.left:
                self.left.addNode(data)
            else:
                self.left=TreeNode(data)
    def levelorder(self):
        root=self
        from collections import deque
        queue=deque()
        queue.append(root)
        while queue:
            root=queue.popleft()
            print(root.data)
            if root.left:queue.append(root.left)
            if root.right:queue.append(root.right)
    def preorder(self):
        stack=[]
        curr=self
        while stack or curr:
            while True:
                if curr:
                    print(curr.data)
                    stack.append(curr)
                    curr=curr.left
                elif stack:
                    curr=stack.pop()
                    curr=curr.right
                else:
                    break
    def postorder(self):
        s1=[]
        s2=[]
        curr=self
        s1.append(curr)
        while s1:
            curr=s1.pop()
            s2.append(curr)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
        while s2:
            print (s2.pop().data)
    def flatten(self):
        root=self
        stack=[]
        stack.append(root)
        while stack:
            root=stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if stack:
                root.right=stack[-1]
            root.left=None
        return root
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

tree=TreeNode(10)
tree.addNode(2)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(6)
tree.addNode(7)
# # tree.levelorder()
# # tree.preorder()
# tree.postorder()
tree.flatten()
# tree.inorder()