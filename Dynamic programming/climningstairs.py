def func(n):
    arr=[1,2]
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    print(arr[n-1])
x=int(input())
func(x)

# def func(n):
#     one,two=1,1
#     for i in range(n-1):
#         temp=one
#         one=one+two
#         two=temp
#     return one