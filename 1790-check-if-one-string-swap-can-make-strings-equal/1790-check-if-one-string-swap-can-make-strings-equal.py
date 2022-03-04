class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        x=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                x.append(i)
            if len(x)>2:
                return False
        if len(x)==1:
            return False
        u,v=x
        if s1[u]==s2[v] and s2[u]==s1[v]:
            return True
        else:
            return False
            