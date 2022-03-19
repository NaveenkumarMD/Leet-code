class Solution:
    def rob(self, nums: List[int]) -> int:
        def robx(nums):
            n=len(nums)
            arr=[0]*n
            if n==0:return 0
            elif n==1:return nums[0]
            arr[0]=nums[0]
            arr[1]=max(nums[0],nums[1])
            for i in range(2,n):
                arr[i]=max(arr[i-1],arr[i-2]+nums[i])
            return arr[n-1]
        x=len(nums)
        arr=nums
        if x==0:
            return 0
        elif x==1:
            return max(arr)
        return max(robx(arr[1:]),robx(arr[:len(arr)-1]))
    
        