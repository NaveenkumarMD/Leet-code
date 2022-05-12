def binarysearch(arr,x):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==x:
            return True
        elif arr[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return False
def counttriplets(arr):
    arr.sort()
    res=0
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if binarysearch(arr,arr[i]+arr[j]):
                print(arr[i],arr[j],arr[i]+arr[j])
                res+=1
    return res
x=[ 2,3,4]
res=counttriplets(x)
print(res)
