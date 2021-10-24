def isAnagram(s: str, t: str) -> bool:
    dit={}
    if len(s)!=len(t):
        return False
    for i in s:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1
    for i in t:
        if i in dit:
            dit[i]-=1
            if dit[i]==0:
                dit.pop(i)
    return len(dit.keys())==0
def isAAnagram(s,t):
    a=sum([ord(i) for i in s])
    b=sum([ord(i) for i in t])
    return a==b
print(isAnagram("naveen","naveen"))