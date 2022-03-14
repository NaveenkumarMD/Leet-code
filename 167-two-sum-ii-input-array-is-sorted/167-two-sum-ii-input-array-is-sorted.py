class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end=0,len(nums)-1
        while start<=end:
            x=nums[start]+nums[end]
            if x==target:
                return [start+1,end+1]
            if x>target:
                end-=1
            else:
                start+=1
            
            
        