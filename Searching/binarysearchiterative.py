def search(arr,x):
    low=0
    mid=0
    high=len(arr)-1
    while low<=high :
        mid=(high+low)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

x=search([1,2,3,4,6,7,8,9,10,11],00)
print(x)
    