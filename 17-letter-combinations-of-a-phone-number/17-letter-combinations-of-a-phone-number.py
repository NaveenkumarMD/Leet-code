class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dit={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        if len(digits)==0:
            return []
        res=[]
        def dfs(i,curr):
            if len(curr)==len(digits):
                return res.append(curr)
            for char in dit[digits[i]]:
                dfs(i+1,curr+char)
        dfs(0,"")
        return res
        