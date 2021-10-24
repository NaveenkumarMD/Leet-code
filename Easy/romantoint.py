def romanToInt(s):
    dit={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"o":0}
    sumx=0
    s+="o"
    for i in range(len(s)-1):
        if(dit[s[i]]<dit[s[i+1]]):
            sumx-=dit[s[i]]
        else:
            sumx+=dit[s[i]]
    return sumx
print(romanToInt("LVIII"))