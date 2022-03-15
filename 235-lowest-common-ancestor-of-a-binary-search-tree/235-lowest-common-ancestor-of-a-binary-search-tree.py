# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)
            return lca
        
        if p.val > root.val and q.val > root.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
            return lca
        
        return root
        