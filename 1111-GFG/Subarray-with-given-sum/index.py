def subarraysum(arr,s):
    currsum=0
    startindex=0
    endindex=0
    n=len(arr)
    for i in range(n):
        while currsum>s and startindex<i-1:
            currsum-=arr[startindex]
            startindex+=1
        if currsum==s:
            return [startindex,endindex]
        if currsum<s:
            currsum+=arr[i]
            endindex+=1
    return [0]

arr=[1, 4, 20, 3, 10, 5]
x=subarraysum(arr,33)
print(x)