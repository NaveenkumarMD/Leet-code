def find(n,k):
    arr=[i for i in range(1,n+1)]
    while len(arr)!=1:
        print(arr)
        for i in range(k-1):
            arr.append(arr.pop(0))
        arr.pop(0)
        
x=find(n=5,k=2)
print(x)