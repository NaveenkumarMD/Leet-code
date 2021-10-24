with open("lastnlines.txt","r+") as fp:
    x=fp.readlines()
    for i in x[-2:]:
        print(i,end="")