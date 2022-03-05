"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def func(self,root,res):
        if root is None:return
        res.append(root.val)
        for i in root.children:
            self.func(i,res)
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        self.func(root,res)
        return res
        

            
        