import math
def findmax(arr):
    max_so_far=-math.inf
    max_here=0
    for i in range(len(arr)):
        max_here+=arr[i]
        if max_here>max_so_far:
            max_so_far=max_here
        if max_here<0:
            max_here=0
    return max_so_far

arr=[-2, -3, 4, -1, -2, 1, 5, -3]
x=findmax(arr)
print(x)