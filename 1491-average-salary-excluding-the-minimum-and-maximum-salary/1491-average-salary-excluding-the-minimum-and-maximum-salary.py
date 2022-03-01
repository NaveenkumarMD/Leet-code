class Solution:
    def average(self, salary: List[int]) -> float:
        x=len(salary)
        y=x-2
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/y