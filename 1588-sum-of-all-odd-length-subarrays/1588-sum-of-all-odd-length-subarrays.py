class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n+1):
                if len(arr[i:j])%2==1:
                    s+=sum(arr[i:j])
        return s
        