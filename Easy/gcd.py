class Solution:
    def findGCD(self, nums) -> int:
        M=max(nums)
        L=min(nums)
        while M!=L:
            if M>L:M=M-L
            else:L=L-M
        print(M)
        return M
x=Solution()
y=x.findGCD([3,99])
print(y)
        