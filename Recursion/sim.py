def shiftmatrix(mat):
    top=0
    bottom=len(mat)-1
    left=0
    right=len(mat[0])-1
    prev=mat[0][0]
    while True:
        if left>right:
            break
        for i in range(left,right+1):
            temp=mat[top][i]
            mat[top][i]=prev
            prev=temp
        top+=1
        if top>bottom:
            break
        for i in range(top,bottom+1):
            temp=mat[i][right]
            mat[i][right]=prev
            prev=temp
        right-=1
        if left>right:
            break
        for i in range(right, left - 1, -1):
            temp = mat[bottom][i]
            mat[bottom][i] = prev
            prev = temp
 
        bottom = bottom - 1
 
        if top > bottom:
            break

        for i in range(bottom, top - 1, -1):
            temp = mat[i][left]
            mat[i][left] = prev
            prev = temp
 
        left = left + 1
    mat[0][0]=prev
    print(mat)

x = shiftmatrix([
    [1, 2,    3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]
)
