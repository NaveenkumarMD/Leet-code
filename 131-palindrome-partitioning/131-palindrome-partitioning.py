class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(x,i,j):
            while i<j:
                if x[i]!=x[j]:
                    return False
                i,j=i+1,j-1
            return True
        res=[]
        def util(i,temp):
            if i==len(s):
                res.append(temp[:])
            for j in range(i,len(s)):
                if ispalindrome(s,i,j):
                    temp.append(s[i:j+1])
                    util(j+1,temp)
                    temp.pop()
        util(0,[])
        return res
                    
        