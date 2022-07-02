def rearrange(arr):
    temp=[0]*len(arr)
    start=0
    end=len(arr)-1
    i=0
    while start<=end:
        if i%2==0:
           temp[i]=arr[end]
           end-=1
        else:
            temp[i]=arr[start]
            start+=1
        i+=1
    return temp
x=rearrange([1,2,3,4,5,6,7])
print(x)