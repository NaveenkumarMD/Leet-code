class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dit={}
        x=sorted(nums)
        y=0
        for i in x:
            if i not in dit:
                dit[i]=y
            y+=1
        res=[]
        for i in nums:
            res.append(dit[i])
        print(res)
        return  res