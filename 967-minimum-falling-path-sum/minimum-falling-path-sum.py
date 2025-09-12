class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i-1][j+1], dp[i-1][j]) + matrix[i][j]
                elif j == cols-1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j] 
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[-1]) 