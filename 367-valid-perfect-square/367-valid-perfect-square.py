class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        end=num//2
        start=1
        if num==1:
            return True
        while start<=end:
            mid=(start+end)//2
            x=mid**2
            if x==num:
                return True
            elif x<num:
                start=mid+1
            else:
                end=mid-1
        return False
                