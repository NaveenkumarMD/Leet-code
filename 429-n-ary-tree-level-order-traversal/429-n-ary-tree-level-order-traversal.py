"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q=[]
        if root is None:
            return
        q.append(root)
        res=[]
        while q:
            x=[]
            for i in range(len(q)):
                node=q.pop(0)
                x.append(node.val)
                for i in node.children:
                    q.append(i)
            res.append(x)
        return res