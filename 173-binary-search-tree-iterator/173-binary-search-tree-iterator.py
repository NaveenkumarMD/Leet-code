# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=[]
        self.inorder(root,self.arr)
    def inorder(self,root,arr):
        if root is None:
            return 
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    def next(self) -> int:
        x=self.arr.pop(0)
        return x       

    def hasNext(self) -> bool:
        return True if len(self.arr)>0 else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()