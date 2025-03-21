class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        no_of_islands = 0
        visited = [[0]*cols for _ in range(rows)] 
        
        def recursive(row, col, visted, grid):
            if (row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col] == '1' and visited[row][col] == 0):
                visited[row][col] = 1
                recursive(row+1, col, visited, grid)
                recursive(row, col+1, visited, grid)
                recursive(row-1, col, visited, grid)
                recursive(row, col-1, visited, grid)
            return

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1' and visited[i][j] == 0):
                    recursive(i, j, visited, grid)
                    no_of_islands += 1
        return no_of_islands