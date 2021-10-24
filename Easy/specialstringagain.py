def palindrome(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i,j=i+1,j-1
    return True
def check(s):
    res=[]
    temp=[]
    def dfs(i):
        if i>=len(s):
            return res.append(temp.copy())
        for j in range(i,len(s)):
            temp.append(s[i:j+1])
            dfs(j+1)
            temp.pop()
    dfs(0)
      
print(check("naveen"))           
        