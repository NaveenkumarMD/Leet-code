class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def getpattern(pattern):
            dit={}
            arr=[]
            for i in range(len(pattern)):
                if pattern[i] not in dit:
                    dit[pattern[i]]=i
                arr.append(dit[pattern[i]])
            return arr
        x=getpattern(list(pattern))
        y=getpattern(s.split(" "))
        return x==y
            