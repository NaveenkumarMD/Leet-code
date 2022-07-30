class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        dit=Counter(nums)
        res=[]
        for i in dit:
            if dit[i]==1:
                res.append(i)
        return res
        