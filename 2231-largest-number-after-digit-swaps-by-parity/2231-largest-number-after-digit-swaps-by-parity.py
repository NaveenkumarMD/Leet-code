class Solution:
    def largestInteger(self, num: int) -> int:
        s=""
        odd=[]
        even=[]
        for i in str(num):
            if int(i)%2==0:
                s+="E"
                even.append(i)
            else:
                s+="O"
                odd.append(i)
        odd.sort(reverse=True)
        even.sort(reverse=True)
        i=0
        x=""
        while i<len(str(num)):
            if s[i]=="E":
                x+=even.pop(0)
            else:
                x+=odd.pop(0)
            i+=1
        return x
        