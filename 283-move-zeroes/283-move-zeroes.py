class Solution:
    def moveZeroes(self, nums) -> None:
        zerocount=nums.count(0)
        i=0
        while i!=len(nums)-zerocount:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:i+=1