def func(arr=[2,7,9,3,1]):
    if len(arr)==0:
        return 0
    if len(arr)<=2:
        return max(arr)
    ans=[0 for _ in range(len(arr))]
    ans[0]=arr[0]
    ans[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        ans[i]=max(ans[i-1],arr[i]+ans[i-2])
    print(ans[len(arr)-1])
func()