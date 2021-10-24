def solve(arr):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(0)
    return arr
if __name__=="__main__":
    x=solve([1,2,3,4,5,0,0,5,6,7])
    print(x)