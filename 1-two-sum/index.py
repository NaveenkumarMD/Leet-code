f=open("x.txt")
x=f.readlines()


v=open("t.txt")
y=v.readlines()

s=[]
for i in x:
    if i not in y:
        s.append(i)
print(s)
