from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            prod*=i
        return self.signFunc(prod)
    def signFunc(self,x):
        if x==0:
            return 0
        return -1 if x<0 else 1