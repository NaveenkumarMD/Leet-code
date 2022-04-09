class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y =len(a) , len(b)
        d=max(x,y)
        a= "0"*(d-x)+a
        b= "0"*(d-y)+b  #making both bin no of equal length
        
        carry="0"
        ans=""
        
        def bin_add(x,y,z): #here x is first no y is second no to be added and z is carry that has to be added
            
            x= 0 if(ord(x)==48) else 1  #converting string to no ascii value of 0 is 48
            y= 0 if(ord(y)==48) else 1
            z= 0 if(ord(z)==48) else 1
            
            if(x==y==z):
                if(x==1):
                    return ['1','1'] # first index is for ans second index for carry
                else:
                    return ['0','0']
            if(x+y+z ==2):
                return ['0','1']
            return ['1','0']
                    
        for i in range(d-1,-1,-1):
            sol=bin_add(a[i],b[i],carry)
            carry=sol[1]
            ans=sol[0]+ans      #appending everything to ans variable 
        
        ans =("1"+ans) if(carry=="1") else ans
        return ans