from heapq import heapify,heappush
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        arr=[]
        while nums:
            arr.append(heappop(nums))
        return arr
        
        