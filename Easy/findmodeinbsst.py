def traverse():
    arr={1:1,2:2}
    ms=0
    ans=[]
    for i,j in arr.items():
        if j>ms:
            ms=j
            ans.clear()
            ans.append(i)            
        elif j==ms:
            ans.append(i)
        else:
            continue
    print(ans)
    print(arr)
traverse()