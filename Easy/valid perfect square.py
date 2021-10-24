class Solution:
    pass
def isPerfectSquare(self, n: int) -> bool:
    if(n==1):
        return True
    value=0
    minx=0
    maxx=n//2
    while(minx<=maxx):
        temp=(minx+maxx)//2
        sqrt=temp**2
        if(sqrt==n):
            return True
        elif sqrt>n:
            maxx=temp-1
        else:
            minx=temp+1
    return False
x=isPerfectSquare(1)
print(x)