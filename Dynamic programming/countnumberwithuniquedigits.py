class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:return 1
        if n==1 :return 10
        arr=[0 for i in range(n+1)]
        arr[0]=1
        arr[1]=9
        x=9
        for i in range(2,n+1):
            arr[i]=x*arr[i-1]
            x-=1
        return sum(arr)
        