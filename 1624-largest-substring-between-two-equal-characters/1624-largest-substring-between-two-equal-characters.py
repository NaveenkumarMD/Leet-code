class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dit={}
        res=-1
        for i,j in enumerate(s):
            if j not in dit:
                dit[j]=i
            elif i-dit[j]-1>res:
                res=i-dit[j]-1
        return res
        