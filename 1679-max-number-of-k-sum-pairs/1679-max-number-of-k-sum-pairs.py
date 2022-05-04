from collections import Counter
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        dit=Counter(nums)
        res=0
        for i in nums:
            if k-i in dit:
                if i==k-i:
                    if dit[i]>1:
                        res+=1
                        dit[i]-=2
                elif dit[i]>0 and dit[k-i]>0:
                    dit[i]-=1
                    dit[k-i]-=1
                    res+=1
        return res