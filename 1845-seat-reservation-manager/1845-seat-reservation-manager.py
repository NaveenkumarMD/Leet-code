from heapq import heapify,heappop,heappush
class SeatManager:

    def __init__(self, n: int):
        self.n=n
        self.arr=[i+1 for i in range(n)]
        heapify(self.arr)

    def reserve(self) -> int:
        return heappop(self.arr)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.arr,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)