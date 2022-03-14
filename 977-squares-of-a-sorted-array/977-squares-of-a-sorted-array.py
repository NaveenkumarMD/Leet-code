class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        res=[0]*(j+1)
        k=j
        while i<=j:
            x,y=nums[i]**2,nums[j]**2
            if x>y:
                res[k]=x
                i+=1
            else:
                res[k]=y
                j-=1
            k-=1
        return res
            
            
        