def check(arr,row,col):
    # We will be placing a single queen in a row,so Its enough to check is there any
    for i in range(col):
        if arr[row][i]==1:
            return False
    
def queens(n):
    pass
x=queens(4)
print(x)