class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num=num1
        arr=num2
        l=len(num)-1
        f=len(arr)-1
        rem=0
        s=[]
        while f>=0 and l>=0:
            temp=int(num[l])+int(arr[f])+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            f-=1
            l-=1
        while f>=0 and l==-1:
            temp=int(arr[f])+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            f-=1
        while l>=0 and f==-1:
            temp=int(num[l])+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            l-=1
        if rem>0:
            s.insert(0,rem)  
        d=""
        for i in s:
            d+=str(i)
        return d
        