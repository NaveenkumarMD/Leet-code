class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-2,2):
            for j in range(0,len(nums)-i-2,2):
                if nums[j]>nums[j+2]:
                    nums[j],nums[j+2]=nums[j+2],nums[j]
        for i in range(1,len(nums)-1,2):
            for j in range(1,len(nums)-i-1,2):
                if nums[j]<nums[j+2]:
                    nums[j],nums[j+2]=nums[j+2],nums[j]
        print(nums)
        return nums