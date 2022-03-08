class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if n*m != r*c :return mat
        reshaped = [[0]*c for _ in range(r)]
        for N in range(r*c):
            i, j = divmod(N, c)
            mati, matj = divmod(N, n)
            reshaped[i][j] = mat[mati][matj]
        return reshaped
        