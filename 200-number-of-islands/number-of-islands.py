class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        noOfIslands = 0
        visited = [[False] * cols for _ in range(rows)]

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited[r][c] = True

            while queue:
                row,col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) and new_col in range(cols)
                        and not visited[new_row][new_col] and grid[new_row][new_col] == '1'):
                        queue.append((new_row,new_col))
                        visited[new_row][new_col] = True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r,c)
                    noOfIslands += 1
        return noOfIslands



    

