class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    def postorderwithoutrecursion(self):
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
            print(s2.pop().val)
    def addnode(self,val):
        if self.val<val:
            if self.left:
                self.left.addnode(val)
            else:
                self.left=TreeNode(val)
        else:
            if self.right:
                self.right.addnode(val)
            else:
                self.right=TreeNode(val)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()
    def inordertraversalwithoutrecursion(self):
        stack=[]
        curr=self
        while curr or stack:
            while True:
                if curr:
                    stack.append(curr)
                    curr=curr.left
                elif(stack):
                    curr=stack.pop()
                    print(curr.val)
                    curr=curr.right
                else:
                    break
    def preordertraversal(self):
        print(self.val)
        if self.left:
            self.left.preordertraversal()
        if self.right:
            self.right.preordertraversal()
    def preorderwithoutrecursion(self):
        stack=[]
        curr=self
        while curr or stack:
            while True:
                if curr:
                    print(curr.val)
                    stack.append(curr)
                    curr=curr.left
                elif(stack):
                    curr=stack.pop()
                    curr=curr.right
                else:
                    break
    def levelorder(self):
        from collections import deque
        queue=deque()
        curr=self
        queue.append(curr)
        while queue:
            curr=queue.popleft()
            print(curr.val)
            if curr.left:queue.append(curr.left)
            if curr.right:queue.append(curr.right)

tree=TreeNode(1)
tree.addnode(2)
tree.addnode(3)
tree.addnode(4)
tree.addnode(5)
tree.addnode(6)
tree.addnode(7)
# tree.inorder()
# tree.inordertraversalwithoutrecursion()
# tree.preorderwithoutrecursion()
# tree.preordertraversal()
# tree.postorderwithoutrecursion()
tree.levelorder()

    # def addNode(self, val):
    #     if val < self.val:
    #         if self.left is None:
    #             self.left = TreeNode(val)
    #         else:
    #             self.left.addNode(val)
    #     else:
    #         if self.right is None:
    #             self.right = TreeNode(val)
    #         else:
    #             self.right.addNode(val)