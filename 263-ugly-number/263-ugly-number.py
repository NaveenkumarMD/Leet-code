class Solution:
    def isUgly(self, n: int) -> bool:
        num=n
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
                
                    