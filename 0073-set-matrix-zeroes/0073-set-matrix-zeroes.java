class Solution {
 public void setZeroes(int[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        boolean[][] isZero=new boolean[rows][cols];

        for(int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                isZero[i][j]=matrix[i][j]==0;
            }
        }
        for(int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if (isZero[i][j]) {
                    for (int c = 0; c < cols; c++) {
                        matrix[i][c] = 0;
                    }
                    for (int r = 0; r < rows; r++) {
                        matrix[r][j] = 0;
                    }
                }
            }
        }

    }
}