# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root,ans):
            if root is None:return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        ans=[]
        inorder(root,ans)
        i,j=0,len(ans)-1
        if len(ans)==1:
            return False
        while i<j:
            x,y=ans[i],ans[j]
            if x+y == k:
                return True
            elif x+y<k:
                i+=1
            else:
                j-=1
        return False
        