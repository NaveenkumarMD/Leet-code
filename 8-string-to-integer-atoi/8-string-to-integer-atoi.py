class Solution:
    def myAtoi(self, s: str) -> int:
        state,value,pos,sign=0,0,0,1
        if len(s)==0:
            return 0
        while pos<len(s):
            curr=s[pos]
            if state==0:
                if curr ==" ":
                    state=0
                elif curr in "+-":
                    state=1
                    sign=1 if curr == "+" else -1
                elif curr.isdigit():
                    state=2
                    value=value*10 +int(curr)
                else:
                    return 0
            elif state==1:
                if curr.isdigit():
                    value=value*10 +int(curr)
                    state=2
                else:
                    return 0
            elif state==2:
                if curr.isdigit():
                    value=value*10+int(curr)
                    state=2
                else:
                    break
            else:
                return 0
            pos+=1
        value=sign*value
        value=min(2**31 -1,value)
        value=max(-(2**31),value)
        return value
                    