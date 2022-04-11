class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=bin(start^goal)
        return x.count("1")