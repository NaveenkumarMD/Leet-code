import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums

    def pick(self, target: int) -> int:
        x=[]
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                x.append(i)
        return x[random.randint(0,len(x)-1)]
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

#can also use(ax+b)mod n