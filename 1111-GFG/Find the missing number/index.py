def findmissing(arr):
    for i in range(len(arr)+1):
        if arr[i]!=i+1:
            return i+1
c=findmissing([1,2,3,4,5,7,8])
print(c)