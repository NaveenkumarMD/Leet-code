class Solution:
    def addToArrayForm(self, num, k: int) :
        l=len(num)-1
        i=0
        arr=[]
        while k>0:
            arr.insert(0,k%10)
            k//=10
        f=len(arr)-1
        rem=0
        s=[]
        while f>=0 and l>=0:
            temp=num[l]+arr[f]+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            f-=1
            l-=1
        while f>=0 and l==-1:
            temp=arr[f]+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            f-=1
        while l>=0 and f==-1:
            temp=num[l]+rem
            if temp>9:
                s.insert(0,temp%10)
                rem=temp//10
            else:
                s.insert(0,temp)
                rem=0
            l-=1
        if rem>0:
            s.insert(0,rem)  
        return s