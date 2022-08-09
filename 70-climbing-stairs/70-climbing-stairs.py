class Solution:
    def climbStairs(self, n: int) -> int:
        arr={}
        def dfs(n):
            if n in arr:
                return arr[n]
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 2
            else:
                arr[n]=dfs(n-1)+dfs(n-2)
                return arr[n]
        return dfs(n)
        
        