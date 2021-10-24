arr=[1,2]

def find(arr):
    x=-999
    y=-999
    for i in arr:
        if i>x:
            x,y=i,x
    return y
print(find(arr))            
