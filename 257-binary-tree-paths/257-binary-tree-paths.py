class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        v = []
        def dfs(tree, s):
            
            if not tree:
                return
            
            if tree.left is None and tree.right is None:
                s += str(tree.val)
                v.append(s)
            
            s += str(tree.val) + '->'
            dfs(tree.left, s)
            dfs(tree.right, s)
        
        dfs(root, "")
        return v