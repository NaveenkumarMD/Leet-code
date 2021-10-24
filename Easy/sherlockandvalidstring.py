from collections import Counter
s="aabbccd"

def check(s):
    dit=Counter(s)
    if len(set(dit.values()))==1:
        return "YES"
    elif len(set(dit.values()))>2:
        return "NO"
    else:
        for i in dit:
            dit[i]-=1
            temp=list(dit.values())
            try:
                temp.remove(0)
            except :
                pass
            if len(set(temp))==1:
                return "YES"
            dit[i]+=1
        return "NO"
print(check("ddddf"))
