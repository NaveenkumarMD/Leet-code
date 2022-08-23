# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack=[]
        stack.append((root,0))
        s=0
        while stack:
            curr,val=stack.pop()
            val=val*10 +curr.val
            if curr.left==None and curr.right==None:
                s+=val
            if curr.right:
                stack.append((curr.right,val))
    
            if curr.left:
                stack.append((curr.left,val))
        return s
