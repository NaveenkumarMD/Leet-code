class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs=sorted(costs,key=lambda x:x[0]-x[1])
        count=0
        x=len(costs)
        print(costs)
        for i in range(len(costs)):
            if i>=x//2:
                count+=costs[i][1]
                print("s")
            else:
                count+=costs[i][0]
        return count
            
        