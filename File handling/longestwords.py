with open("longestwords.txt","r+") as fp:
    x=fp.read().split()
    for i in x:
        if len(i)==len(max(x,key=len)) :
            print(i)