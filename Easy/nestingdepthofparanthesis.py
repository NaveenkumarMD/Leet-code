def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
rotate_num=int(input())
print(rotateArray(arr, n, rotate_num))