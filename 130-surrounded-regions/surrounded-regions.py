class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def marker(r,c):
            if (c<0 or r<0 or c==COLS or r==ROWS or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            marker(r+1, c)
            marker(r-1, c)
            marker(r, c+1)
            marker(r, c-1)

        for r in range(ROWS):
            marker(r, 0)
            marker(r, COLS-1)

        for c in range(COLS):
            marker(0, c)
            marker(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'