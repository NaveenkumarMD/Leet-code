class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s=s+str(i)
        s=str(int(s)+1)
        return list(s)
        
        