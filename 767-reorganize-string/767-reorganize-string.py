from collections import Counter
from heapq import heapify,heappop,heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        dit=Counter(s)
        arr=[[-count,char] for char,count in  dit.items()]
        heapify(arr)
        res=""
        prev=""
        while arr or prev:
            if prev and not arr:
                return ""
            count,char=heappop(arr)
            count+=1
            res+=char
            if prev:
                heappush(arr,prev)
                prev=None
            if count!=0:
                prev=[count,char]
        return res

        
        