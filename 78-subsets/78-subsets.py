class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(first=0,curr=[]):
            if len(curr)==k:
                return res.append(curr[:])
            for i in range(first,n):
                curr.append(nums[i])
                back(i+1,curr)
                curr.pop()
        n=len(nums)
        for k in range(len(nums)+1):
            back()
        return res