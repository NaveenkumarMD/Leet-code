class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        print(costs)
        x=0
        i=0
        while x<coins and i<len(costs):
            temp=costs[i]+x
            if temp<=coins:
                x=temp
                i+=1
            else:
                break
        return i