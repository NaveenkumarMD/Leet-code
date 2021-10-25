from typing import List
from heapq import heapify,heappop

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dit={}
        for i,j in enumerate(score):
            dit[j]=i
        x=score[:]
        heapify(x)
        n=len(score)
        for i in range(n):
            tempscore=heappop(x)
            rank=n-i
            tempindex=dit[tempscore]
            
            if rank==1:
                score[tempindex]="Gold Medal"
                continue
            if rank==2:
                score[tempindex]="Silver Medal"
                continue
            if rank==3:
                score[tempindex]="Bronze Medal"
                continue
            score[tempindex]=str(rank)
        print(score)
        return score

        
x=Solution()
y=x.findRelativeRanks(score = [10,3,8,9,4])
print(y)