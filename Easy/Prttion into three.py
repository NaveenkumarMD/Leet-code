arr=[1,2,3,4,5,6,7,8,9,10]

def check(arr):
    total=sum(arr)
    if total%3!=0:
        return False
    div=total/3
    s=0
    c=0
    for i in arr:
        s+=i
        if s==div:
            s=0
            c+=1
        if c==3:
            return True
    return c==3
x=check(arr)
print(x)