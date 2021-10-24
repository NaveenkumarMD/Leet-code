from collections import Counter
with open("longestwords.txt","r" ) as fp:
    x=fp.read().split()
    # x=Counter(x)
    # print(x)
    dit={}
    for i in x:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1
    print(dit)