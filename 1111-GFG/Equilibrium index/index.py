def equilibrium(arr):
    totalsum=sum(arr)
    leftsum=0
    for i in range(len(arr)):
        totalsum-=arr[i]
        if totalsum==leftsum:
            return i
        leftsum+=arr[i]
    return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
x=equilibrium(arr)
print(x)