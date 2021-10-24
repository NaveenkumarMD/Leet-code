def generate(numRows):
    arr=[[0]*i for i in range(1,numRows+1)]
    print(arr)
    arr[0]=[1]
    arr[1]=[1,1]
    for i in range(2,numRows):
        arr[i][0]=1
        arr[i][i]=1
        for j in range(1,i):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    print(arr)
    return arr
for i in range(3):
    generate(int(input()))