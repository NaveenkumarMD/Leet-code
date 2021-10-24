def makeFancyString(self, s):
    str=s[0]
    count=0
    for i in range(1,len(s)):
        if(s[i-1]==s[i]):
            count+=1
        else:
            count=0
        if(count<2):
            str=str+s[i]
    return (str)