if __name__=="__main__":
    def check(arr):
        res=[]
        temp=[]      
        def dfs(i):
            if i>=len(arr):
                return res.append(temp.copy())
            for j in range(i,len(arr)):
                if(palindromecheck(arr,i,j)):
                    temp.append(arr[i:j+1])
                    dfs(j+1)
                    temp.pop()
        dfs(0)
        return res

    def palindromecheck(arr,l,r):
        while l<r :
            if arr[l]!=arr[r]:
                return False
            else:
                r,l=r-1,l+1
        return True
    x=check("aab")
    print(x)            