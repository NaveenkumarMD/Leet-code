def search(arr,x,low,high):
    if low<=high:
        mid=(low+high )//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return search(arr,x,low,mid-1)
        else:
            return search(arr,x,mid+1,high)
    else:
        return -1
print(search([1,2,3,4,5],4,0,len([1,2,3,4,5])-1))