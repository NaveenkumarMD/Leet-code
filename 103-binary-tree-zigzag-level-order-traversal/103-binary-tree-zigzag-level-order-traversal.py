# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        q.append(root)
        res=[]
        if root is None:
            return []
        flag=False
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not flag:
                res.append(temp)
            else:
                res.append(temp[::-1])
            flag=not flag
        return res
                