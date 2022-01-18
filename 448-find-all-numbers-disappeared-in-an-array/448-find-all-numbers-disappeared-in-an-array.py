class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=len(nums)
        dict={i:False for i in range(1,x+1)}
        for i in nums:
            dict[i]=True
        return [i for i,j in dict.items() if j==False]
        