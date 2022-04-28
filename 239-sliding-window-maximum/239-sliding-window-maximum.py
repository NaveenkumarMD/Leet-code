from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(len(nums)):
            while q and q[-1][1]<nums[i]:
                q.pop()
            q.append((i,nums[i]))
            while i-q[0][0]+1>k:
                q.popleft()
            if i+1>=k:
                res.append(q[0][1])
        return res
            
            
