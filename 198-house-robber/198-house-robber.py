class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0 for _ in range(len(nums))]
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[-1]
        arr[0]=nums[0]
        arr[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            arr[i]=max(arr[i-1],nums[i]+arr[i-2])
        print(arr)
        return arr[n-1]
        