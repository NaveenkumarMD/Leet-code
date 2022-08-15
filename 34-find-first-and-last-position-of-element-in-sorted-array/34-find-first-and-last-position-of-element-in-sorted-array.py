class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        if len(nums)==0:
            return [-1,-1]
        j=len(nums)-1
        res=[-1,-1]
        while i<j:
            mid=(i+j)//2
            if nums[mid]<target:
                i=mid+1
            else:
                j=mid
        if nums[i]!=target:
            return res
        else:
            res[0]=i
        j=len(nums)-1
        while i<j:
            mid=(i+j)//2 +1
            if nums[mid]>target:
                j=mid-1
            else:
                i=mid
        if nums[j]!=target:
            return res
        else:
            res[1]=j
        return res
        
        