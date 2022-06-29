class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dit={}
        for idx,val in enumerate(order):
            dit[val]=idx
        x=[]
        arr=list(s)
        y=""
        for i in arr:
            if i in dit:
                x.append(i)
            else:
                y+=i
                
        print(dit)
        print(x)
        for i in range(len(x)):
            for j in range(i,len(x)):
                if dit[x[i]]>dit[x[j]]:
                    x[i],x[j]=x[j],x[i]
        return "".join(x)+y