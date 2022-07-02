def maxplatforms(arr,dep):
    res=0
    plat=1
    i=1
    j=0
    while i<len(arr) and j<len(arr):
        if arr[i]<=dep[j]:
            plat+=1
            i+=1
        elif arr[i]>dep[j]:
            plat-=1
            j+=1
        res=max(plat,res)
    return res

x=maxplatforms([900, 940, 950, 1100, 1500, 1800 ], [910, 1200, 1120, 1130, 1900, 2000 ])
print(x)