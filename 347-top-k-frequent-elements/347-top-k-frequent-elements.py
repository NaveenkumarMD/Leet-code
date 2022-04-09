class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit={}
        for i in nums:
            if i not in dit:
                dit[i]=1
            else:
                dit[i]+=1
        dit=sorted(dit,key=dit.get,reverse=True)
        return dit[:k]
        