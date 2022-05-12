class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        x=nums.copy()
        x.sort()
        i=0
        j=len(nums)-1
        while i<len(nums) and nums[i]==x[i]:
            i+=1
        while j>=0 and nums[j]==x[j]:
            j-=1
        return j-i+1 if j>=i else 0