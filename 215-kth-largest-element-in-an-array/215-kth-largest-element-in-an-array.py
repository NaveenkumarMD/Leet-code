class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify,heappop
        arr=[-i for i in nums]
        heapify(arr)
        res=0
        for i in range(k):
            res=-(heappop(arr))
        return res
            
        