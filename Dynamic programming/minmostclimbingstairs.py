class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        arr=[0 for _ in range(n)]
        arr[0]=cost[0]
        arr[1]=cost[1]
        for i in range(2,n):
            arr[i]=min(arr[i-1]+cost[i],cost[i]+arr[i-2])
        return min(arr[-1],arr[-2])