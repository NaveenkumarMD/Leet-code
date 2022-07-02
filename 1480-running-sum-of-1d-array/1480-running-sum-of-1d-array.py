class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        res=[]
        for i in nums:
            res.append(temp+i)
            temp+=i
        return res