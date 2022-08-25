# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def search(arr,start,end,value):
            for i in range(start,end+1):
                if arr[i]==value:
                    return i
        self.curr=0
        def buildtrees(inorder,preorder,instart,inend):
            if instart>inend:
                return None
            tnode=TreeNode(preorder[self.curr])
            self.curr+=1
            inidx=search(inorder,instart,inend,tnode.val)
            tnode.left=buildtrees(inorder,preorder,instart,inidx-1)
            tnode.right=buildtrees(inorder,preorder,inidx+1,inend)
            return tnode
        root=buildtrees(inorder,preorder,0,len(preorder)-1)
        return root