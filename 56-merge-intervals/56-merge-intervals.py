class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        merged.append(intervals[0])
        for i in range(1,len(intervals)):
            print(merged[-1])
            
            if intervals[i][0]<=merged[-1][1]:
                merged[-1][1]=max(intervals[i][1],merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged