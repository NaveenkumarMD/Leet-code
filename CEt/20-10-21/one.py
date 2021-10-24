def solve(x):
    i=1
    odd=0
    even=0
    while x>0:
        if i%2==0:
            even+=x%10
        else:
            odd+=x%10
        i+=1
        x//=10
    return abs(even-odd)
if __name__=="__main__":
    x=solve(int(input()))
    print(x)