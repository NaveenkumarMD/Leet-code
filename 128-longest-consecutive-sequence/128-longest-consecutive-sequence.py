class Solution:
    def longestConsecutive(self, nums) -> int:
        s=list(set(nums))
        if not nums:
            return 0
        s.sort()
        res=0
        temp=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]-1:
                temp+=1
            else:
                res=max(res,temp)
                temp=0
        res=max(res,temp)
        return res+1
                