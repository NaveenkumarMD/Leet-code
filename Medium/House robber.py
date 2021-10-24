def rob(nums):
    n=len(nums)
    arr=[0]*(n)
    if n==0:
        return 0
    if n==1:
        return nums[1]
    arr[0]=nums[0]
    arr[1]=max(nums[0],nums[1])
    for i in range(2,n):
        arr[i]=max(arr[i-1],nums[i]+arr[i-2])
    return arr    
res=rob([2,1,1,2])
print(res)