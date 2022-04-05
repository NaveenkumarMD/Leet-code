class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive,negative=0,1
        arr=[0]*len(nums)
        for i in nums:
            if i<0:
                arr[negative]=i
                negative+=2
            else:
                arr[positive]=i
                positive+=2
        return arr
                