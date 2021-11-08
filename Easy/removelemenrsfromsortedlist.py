class Solution:
    def removeDuplicates(self, nums) -> int:
        index=0
        for num in nums:
            if num!=nums[index]:
                index+=1
                nums[index]=num
        return index+1
        
x=Solution()
y=x.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])