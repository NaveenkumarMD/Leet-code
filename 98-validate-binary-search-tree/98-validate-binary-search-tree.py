# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root,ans):
            if root is None:
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        arr=[]
        inorder(root,arr)
        for i in range(1,len(arr)):
            if not arr[i-1]<arr[i]:
                return False
        return True
        