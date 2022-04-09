class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(a,b):
            if a=='1' and b=='1':
                return ('0','1')
            elif a=='0' and b=='0':
                return ('0','0')
            else:
                return ('1','0')
        m=max(len(a),len(b))
        if len(a)<m:
            a='0'*abs(len(a)-m)+a
        if len(b)<m:
            b='0'*abs(len(b)-m)+b
        s=""
        carry='0'
        for i in range(m-1,-1,-1):
            x,y=a[i],b[i]
            v,r=add(x,y)
            if carry=='1':
                v,r=add('1',v)
            carry=r
            s+=v
        if carry=='1':
            s+='1'
        # return s[::-1]
        print(s[::-1])
                          
                
            
x=Solution()
y=x.addBinary(a="1010", b="1011")