# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        res=0
        while queue:
            node=queue.popleft()
            if node:
                if node.left and not node.left.left and not node.left.right:
                    res+=node.left.val
                queue.append(node.left)
                queue.append(node.right)
        return res