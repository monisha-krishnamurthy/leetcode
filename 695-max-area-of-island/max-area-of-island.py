class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        maxArea = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            visited[r][c] = True
            area = grid[r][c]

            while queue:
                (row, col) = queue.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == 1 and visited[new_row][new_col] == False):
                            area += grid[new_row][new_col]
                            visited[new_row][new_col] = True
                            queue.append((new_row,new_col))
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == False:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea