class Solution:
    def hammingWeight(self, n: int) -> int:
        x=str(bin(n))
        return x.count("1")
        