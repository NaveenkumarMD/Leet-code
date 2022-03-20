#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        sum_=s
        curr_sum = arr[0]
        start = 0
     
        # Add elements one by
        # one to curr_sum and
        # if the curr_sum exceeds
        # the sum, then remove
        # starting element
        i = 1
        while i <= n:
             
            # If curr_sum exceeds
            # the sum, then remove
            # the starting elements
            while curr_sum > sum_ and start < i-1:
             
                curr_sum = curr_sum - arr[start]
                start += 1
                 
            # If curr_sum becomes
            # equal to sum, then
            # return true
            if curr_sum == sum_:

                return [start+1,i]
     
            # Add this element
            # to curr_sum
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
     
        # If we reach here,
        # then no subarray
        return [-1]
               

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends