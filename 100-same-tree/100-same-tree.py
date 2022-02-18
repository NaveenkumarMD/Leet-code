# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        queue=[]
        queue1=[]
        queue.append(p)
        queue1.append(q)
        while queue and queue1:
            root=queue.pop(0)
            root1=queue1.pop(0)
            
            if root and root1 and root1.val!=root.val:
                return False
            if root.left is not None and root1.left is not None:
                queue.append(root.left)
                queue1.append(root1.left)
            if root.right is not None and root1.right is not None:
                queue.append(root.right)
                queue1.append(root1.right)
            if (root.left and not root1.left) or (root1.left and not root.left) or(root1.right and not root.right) or (root.right and not root1.right):
                return False
        return True
        
        