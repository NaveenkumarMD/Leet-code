def uniquepaths(m,n,dit={}):
    key=str(m)+","+str(n)
    if key in dit :return dit[key]
    if m==0 or n==0:
        return 0
    if n==1 and n==1:
        return 1
    dit[key]=uniquepaths(m-1,n,dit)+uniquepaths(m,n-1,dit)
    return dit[key]
x=uniquepaths(70,23)
print(x)