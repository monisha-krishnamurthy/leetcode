class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh>0:
            flag = False
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc                            
                            if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                                grid[nr][nc] = 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1 

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            time += 1

        return time
