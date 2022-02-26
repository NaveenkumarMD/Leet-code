#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        dit=[[start[x],end[x]] for x in range(n)]
        dit.sort(key=lambda x: x[1])
        last_time=dit[0][1]
        arr=[]
        arr.append(0)
        for i in range(1,n):
            if dit[i][0]>last_time:
                arr.append(i)
                last_time=dit[i][1]
        return len(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends