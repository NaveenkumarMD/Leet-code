# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True
        def height(root):
            if root is None:
                return 0
            l=height(root.left)
            r=height(root.right)
            if self.res  and abs(l-r)>1:
                self.res=False
                
            return max(l,r)+1
        height(root)
        return self.res
                
        