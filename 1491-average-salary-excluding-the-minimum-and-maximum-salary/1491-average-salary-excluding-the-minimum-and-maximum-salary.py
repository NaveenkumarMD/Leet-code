class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        max=-1
        min=999999999
        for i in salary:
            if i>max:
                max=i
            if i<min:
                min=i
        return sum([i for i in salary if i not in [min,max]])/(n-2)
        
        