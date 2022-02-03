class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        result=[0]*n
        G=[[] for i in range(n)]
        for i,j in paths:
            G[i-1].append(j-1)
            G[j-1].append(i-1)
        for i in range(n):
            result[i]=({1,2,3,4}-{result[j] for j in G[i]}).pop()
        return result