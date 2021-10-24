from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        try:
            return max([i for i,j in Counter(arr).items() if i==j]) 
        except:
            return -1
            

        