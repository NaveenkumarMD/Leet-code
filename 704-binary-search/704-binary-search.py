class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+(end-start)
            if target==nums[mid]:
                return mid
            if nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return -1
                
                
        