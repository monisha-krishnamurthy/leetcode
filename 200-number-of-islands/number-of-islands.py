class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        noOfIslands = 0

        def dfs(i, j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                dfs(i+dr, j+dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    noOfIslands += 1
        return noOfIslands

