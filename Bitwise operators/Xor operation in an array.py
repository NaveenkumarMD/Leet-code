class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=start
        arr=[]
        s=start
        while n>0:
            s+=2
            n-=1
            if(n==0):
                break
            print(s)
            res=s^res
        print(res)
x=Solution()
y=x.xorOperation(5,0)