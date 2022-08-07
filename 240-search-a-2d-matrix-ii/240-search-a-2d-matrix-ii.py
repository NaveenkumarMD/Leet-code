class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

		# base case
		if len(matrix) == 0 or (len(matrix)==1 and len(matrix[0])==0):
			return False
		M, N = len(matrix), len(matrix[0])

		if M == 1 and N == 1:
			return True if matrix[0][0]==target else False

		# divide and conquer
		mid_M = M if M == 1 else M // 2
		mid_N = N if N == 1 else N // 2

		top_l = self.searchMatrix([row[0:mid_N] for row in matrix[0:mid_M]], target)
		top_r = self.searchMatrix([row[mid_N:] for row in matrix[0:mid_M]], target)
		bot_l = self.searchMatrix([row[0:mid_N] for row in matrix[mid_M:]], target)
		bot_r = self.searchMatrix([row[mid_N:] for row in matrix[mid_M:]], target)

		return top_l or top_r or bot_l or bot_r