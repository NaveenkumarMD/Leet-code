# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        import queue
        if not root:
            return 0

        q = []
        q.append((1, root))
        while q:
            level, node = q.pop(0)
            if not node.left and not node.right:
                return level
            
            if node.left:
                q.append((level+1, node.left))
                
            if node.right:
                q.append((level+1, node.right))
            
            
        