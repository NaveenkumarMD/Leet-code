import math
def leaders(arr):
    res=[]
    maxx=-math.inf
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>maxx:
            maxx=arr[i]
            res.append(arr[i])
    return res[::-1]
        

x=leaders(arr=[16, 17, 4, 3, 5, 2])
print(x)