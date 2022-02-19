# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=1
        result=[]
        heightx=self.height(root)
        while level<=heightx:
            temp=[]
            temp1=self.printorder(root,level,temp)
            print(temp1)
            level+=1
            result.append(temp1)
            print(temp1)
            print("ers is ",result)
            temp1=[]
        return result
    def printorder(self,root,level,temp):
        if root is None:
            return
        if level==1:
            temp.append(root.val)
        else:
            self.printorder(root.left,level-1,temp)
            self.printorder(root.right,level-1,temp)
        return temp
    def height(self,root):
        if root is None:
            return 0
        else:
            lheight=self.height(root.left)
            rheight=self.height(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1