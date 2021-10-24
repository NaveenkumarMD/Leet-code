def combinationsum(arr,target):
    res=[]
    def dfs(i,temp,total):
        if total==target:
            return res.append(temp.copy())
        if total>target or i>=len(arr):
            return
        temp.append(arr[i])
        dfs(i,temp,total+arr[i])
        temp.pop()
        dfs(i+1,temp,total)
    dfs(0,[],0)
    return res
x=combinationsum([1,2,3],7) 
print(x)        