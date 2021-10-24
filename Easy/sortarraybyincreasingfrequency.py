import functools
from typing import Collection, List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dit=Counter(nums)
        def compare(x,y):
            if dit[x]<=dit[y]:
                return -1
            if dit[x]>dit[y]:
                return 1
            else:
                return 0

        x=nums.sort(key=functools.cmp_to_key(compare))
        print(nums)
x=Solution()
y=x.frequencySort([2,3,1,3,2])
print(y)
        