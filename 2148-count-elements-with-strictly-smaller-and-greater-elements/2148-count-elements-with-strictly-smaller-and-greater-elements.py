class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if any([i<j for j in nums]) and any([i>j for j in nums]):
                count+=1
        return count
                