class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(source, visit):
            q = deque(source)
            while q:
                r,c = q.popleft()
                visit[r][c] = True
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not visit[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr,nc))
        
        pacSource = []
        atlSource = []
        for c in range(COLS):
            pacSource.append((0,c))
            atlSource.append((ROWS-1, c))

        for r in range(ROWS):
            pacSource.append((r, 0))
            atlSource.append((r, COLS-1))

        bfs(pacSource, pacific)
        bfs(atlSource, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])

        return res