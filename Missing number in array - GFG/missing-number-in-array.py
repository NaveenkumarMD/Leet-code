#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        arr=[i+1 for i in range(n)]
        arr=set(arr)
        array=set(array)
        x=list((arr-array))
        return x[0]
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends