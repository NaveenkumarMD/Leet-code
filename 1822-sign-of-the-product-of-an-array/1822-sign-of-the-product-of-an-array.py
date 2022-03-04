class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i<0:
                count+=1
            elif i==0:
                return 0
        if count%2==1:
            return -1
        return 1
        
        