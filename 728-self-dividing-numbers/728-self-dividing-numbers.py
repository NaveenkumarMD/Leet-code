class Solution:
    def getdigits(self,num):
        arr=[]
        while num>0:
            arr.append(num%10)
            num=num//10
        return arr
    def selfDividingNumbers(self, left: int, right: int) :
        out=[]
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            x=self.getdigits(i)
            flag=True
            for j in x:
                if i%j!=0:
                    flag=False
                    break
            if flag:
                out.append(i)
        return out 
                
            
        
        