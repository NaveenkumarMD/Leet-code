from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for idx,val in enumerate(nums):
            while (q and q[-1][1]<val):
                q.pop()
            q.append((idx,val))
            while idx-q[0][0]+1>k:
                q.popleft()
            if idx+1>=k:
                res.append(q[0][1])
        return res
            
            
