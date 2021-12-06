def func(arr):
    if len(arr)==0:return 0
    if len(arr)<2:return max(arr)
    ans=[0]*len(arr)
    ans[0]=arr[0]
    ans[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        ans[i]=max(ans[i-1],arr[i]+ans[i-2])
    return ans[len(arr)-1]
arr=[1,3,4]


print(max(func(arr[:len(arr)-1]),func(arr[1:])))
