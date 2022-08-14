# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.m=0
        self.res=[]
        def dfs(root,level):
            if root is None:
                return 
            if level>self.m:
                self.res.append(root.val)
                self.m=level
            dfs(root.right,level+1)
            dfs(root.left,level+1)
        dfs(root,1)
        return self.res
                
            