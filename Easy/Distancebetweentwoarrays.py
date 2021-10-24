from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            x=True
            for j in arr2:
                if abs(i-j) <=d:
                    x=False
            if not x:
                c+=1
        return len(arr1)-c

c=Solution()
c.findTheDistanceValue()