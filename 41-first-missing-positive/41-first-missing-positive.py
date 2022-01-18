class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict={}
        max=0
        for i in nums:
            if(i>max):max=i
            if(i>0):
                dict[i]=True
                
        for i in range(1,max+1):
            try:
                x=dict[i]
            except:
                return i
        return max+1
        
        
        