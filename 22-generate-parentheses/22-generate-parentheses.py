class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(o,c,temp):
            if o==c==n:
                res.append(temp[:])
                return
            else:
                if o<n:
                    dfs(o+1,c,temp+"(")
                if c<o:

                    dfs(o,c+1,temp+")")
        dfs(0,0,"")
        return res
        