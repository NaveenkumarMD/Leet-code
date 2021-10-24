def solve(str):
    dit={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
    x=0
    total=0
    for i in range(len(str)-1,-1,-1):
        try:
            if(10>int(str[i])>0 ):
                temp=int(str[i])
        except:
            temp=dit[str[i]]
        total+=temp*(16**x)
        x+=1
    return total
if __name__=="__main__":
    x=solve(input())
    print(x)