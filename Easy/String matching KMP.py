def search(text,pat):
    n=len(text)
    m=len(pat)
    lps=[0]*m
    computelps(pat,m,lps)
    i=0
    j=0
    while i<n:
        if(text[i]==pat[j]):
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
        if j==m:
            return True
    return False
def computelps(pat,m,lps):
    l=0
    i=1
    while(i<m):
        if(pat[l]==pat[i]):
            lps[i]=l+1
            i+=1
            l+=1
        else:
            if(l!=0):
                l=lps[l-1]
            lps[i]=0
            i+=1
    print(lps)

text="aaabcdefghaaaaaaaf"
pat="fgha"
x=search(text,pat)

print(x)