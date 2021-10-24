def check(n):
    if(-2**31 > n > 2**31 - 1):
        return 0
    flag=1
    if(n<0):
        flag=-1
        n=n*-1
    c=0
    while(n>0):
        c=c*10+(n%10)
        n=n//10
    return flag*c
print(check(-3450))