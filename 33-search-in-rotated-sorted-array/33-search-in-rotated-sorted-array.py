class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j )//2
            if nums[mid]==target:
                return mid
            elif nums[i]<=nums[mid]:
                if nums[i]<=target and nums[mid]>=target:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if nums[mid]<=target and nums[j]>=target:
                    i=mid+1
                else:
                    j=mid-1
        return -1
                
                