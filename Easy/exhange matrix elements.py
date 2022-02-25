def fun(matrix):
    for i in range(r):
        # if i is even exchange the last and first element
        if i % 2 == 0:
            matrix[i][0], matrix[i][c - 1] = matrix[i][c - 1], matrix[i][0]
        # else exchange the second and last but one element in that row
        else:
            matrix[i][1], matrix[i][c - 2] = matrix[i][c - 2], matrix[i][1]

    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()


# get row and column input
r, c = map(int, input().split())
# create a list of lists
matrix = []
# get input for each row
for i in range(r):
    matrix.append(list(map(int, input().split())))

fun(matrix)

