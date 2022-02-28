import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = sorted(nums)[-self.k:]
        heapq.heapify(self.stream)

    def add(self, val: int) -> int:
        if len(self.stream)==self.k:
            if val<= self.stream[0]:
                return self.stream[0]
            else:
                heapq.heappop(self.stream)
                heapq.heappush(self.stream,val)
                return self.stream[0]
        else:
            heapq.heappush(self.stream,val)
            if len(self.stream)==self.k:
                return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)