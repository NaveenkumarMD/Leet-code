def rev(arr,k):
    i=0
    n=len(arr)
    while i<n:
        left=i
        right=min(i+k-1,n-1)
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        i+=k
    return arr
arr=[1,2,3,4,5,6,7,8,9]
k=3
print(rev(arr,k))