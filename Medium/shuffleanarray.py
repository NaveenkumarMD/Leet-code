import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums

    def reset(self) -> List[int]:
        return self.arr
        

    def shuffle(self) -> List[int]:
        temp=self.arr[:]
        for i in range(len(temp)):
            x=random.randint(0,len(temp)-1)
            temp[x],temp[i]=temp[i],temp[x]
        return temp
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()