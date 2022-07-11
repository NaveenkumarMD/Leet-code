class Solution:
    def getdigits(self,x):
        s=0
        while x>0:
            x//=10
            s+=1
        return s
    def findNumbers(self, nums: List[int]) -> int:
        nums=[i for i in nums if self.getdigits(i)%2==0]
        return len(nums)
