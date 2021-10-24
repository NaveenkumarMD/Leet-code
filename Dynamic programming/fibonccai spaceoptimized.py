class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return 0
        elif n<=2:
            return 1
        else:
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
            return b
            
        