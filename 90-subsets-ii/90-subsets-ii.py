class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(first=0,curr=[]):
            if len(curr)==k:
                if sorted(curr[:]) not in res:res.append(sorted(curr[:]))
                return
            for i in range(first,n):
                curr.append(nums[i])
                back(i+1,curr)
                curr.pop()
        n=len(nums)
        for k in range(n+1):
            back()
        return res
        