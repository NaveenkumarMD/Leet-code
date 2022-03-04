class Solution(object):
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if(arr[i]+arr[j]==target):
                    if(i!=j):
                        return list((i,j))