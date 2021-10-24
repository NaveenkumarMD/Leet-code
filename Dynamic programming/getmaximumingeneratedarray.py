class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr=[0  for _ in range(n)]
        arr[0]=0
        arr[1]=1
        for i in range(2,n):
            if i%2==0:
                arr[i]=arr[i//2]
            else:
                arr[i]=arr[i//2]+arr[i-(i//2)]
        return max(arr)

s=Solution()