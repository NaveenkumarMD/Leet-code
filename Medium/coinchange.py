import math
def coinchange(coins,amount):
    if(amount<1):return 0
    arr=[math.inf]*(amount+1)
    arr[0]=0
    for i in coins:
        for j in range(i,amount+1):
            if(arr[j-i]!=math.inf):
                arr[j]=min(arr[j],arr[j-i]+1)
                print(arr)
    return arr[8]
x=coinchange([3,4,7],8)
print(x)