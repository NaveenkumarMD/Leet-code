# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        curr=root
        while True:
            if curr.val<val:
                if curr.right is not None:
                    curr=curr.right
                else:
                    curr.right=TreeNode(val)
                    break
            else:
                if curr.left is not None:
                    curr=curr.left
                else:
                    curr.left=TreeNode(val)
                    break
        return root