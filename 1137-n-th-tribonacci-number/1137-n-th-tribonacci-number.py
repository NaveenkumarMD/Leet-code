class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[0,1,1]
        for i in range(3,n+1):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        return arr[n]
        