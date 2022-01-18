class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        arr=[]
        for i in nums:
            if i in dict:
                arr.append(i)
            else:
                dict[i]=True
        return arr
        