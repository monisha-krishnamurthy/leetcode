class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            setI = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in setI:
                    return False
                setI.add(board[i][j])

        
        for i in range(len(board[0])):
            setJ = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in setJ:
                    return False
                setJ.add(board[j][i])

        for square in range(9):
            set3 = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in set3:
                        return False
                    set3.add(board[row][col])
        return True
