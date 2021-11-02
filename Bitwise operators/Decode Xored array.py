class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        temp=first
        for i in encoded:
            temp=temp^i
            arr.append(temp)
        return arr
                
        