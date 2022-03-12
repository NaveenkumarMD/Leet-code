class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=[(bin(i).count("1"),i) for i in arr]
        res.sort()
        return [i[1] for i in res]

        