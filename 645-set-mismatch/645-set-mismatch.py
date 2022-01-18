class Solution:
    def findErrorNums(self, nums):
        for i in range(1,len(nums)+1):
            if i not in nums:
                x=i
                break
        for i in nums:
            if nums.count(i)==2:
                y=i
                break
        return [y,x]
        
