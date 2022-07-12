class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=nums[:]
        suf=nums[:]
        for i in range(1,len(nums)):
            pref[i]=pref[i]*pref[i-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i]*suf[i+1]
        k=0
        arr=[]
        for i in range(len(nums)):
            if i-1 <0:
                l=1
            else:
                l=pref[i-1]
            if i+1 >=len(nums):
                r=1
            else:
                r=suf[i+1]
            arr.append(l*r)
        return arr