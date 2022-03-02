from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dit={}
        for idx,num in enumerate(nums):
            if num in dit:
                if abs(dit[num]-idx)<=k:
                    return True
                else:
                    dit[num]=idx
                
            else:
                dit[num]=idx

        return False
                