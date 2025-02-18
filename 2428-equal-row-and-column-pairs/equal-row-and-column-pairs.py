class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        hashmap = dict()
        m = len(grid)
        n = len(grid[0])
        for col_i in range(n):
            temp = []
            for row_i in range(m):
                temp.append(grid[row_i][col_i])
            temp = tuple(temp)
            if temp in hashmap:
                hashmap[temp] +=1
            else: 
                hashmap[temp] = 1

        for row_i in range(m):
            row = grid[row_i]
            row = tuple(row)
            if row in hashmap:
                pairs = pairs + hashmap[row]

        return pairs