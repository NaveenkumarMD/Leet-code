class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        arr=[0]*n
        stack=[]
        for curr_day,curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<curr_temp:
                prev_day=stack.pop()
                arr[prev_day]=curr_day-prev_day
            stack.append(curr_day)
        return arr