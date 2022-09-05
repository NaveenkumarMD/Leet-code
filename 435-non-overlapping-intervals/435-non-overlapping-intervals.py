class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        if len(intervals)==0:
            return 0
        currlast=intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<currlast:
                count+=1
            else:
                currlast=intervals[i][1]
        return count
        