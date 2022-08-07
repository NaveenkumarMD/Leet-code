class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr=customers[0][0]
        count=0
        s=0
        for i in range(len(customers)):
            if customers[i][0]<=curr:
                curr+=customers[i][1]
                s+=curr-customers[i][0]
            else:
                curr=customers[i][0]
                s+=customers[i][1]
                curr+=customers[i][1]
            count+=1
        return s/count