class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dit=defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                dit[nums[i]*nums[j]]+=1
        res=0
        for x in dit:
            if dit[x]>1:
                res+=4*(dit[x]*(dit[x]-1))
        print(dit)
        return res