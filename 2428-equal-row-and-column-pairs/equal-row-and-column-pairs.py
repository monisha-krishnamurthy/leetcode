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
            if tuple(temp) in hashmap:
                hashmap[tuple(temp)] +=1
            else: 
                hashmap[tuple(temp)] = 1
        print(hashmap)

        for row_i in range(m):
            row = grid[row_i]
            if tuple(row) in hashmap:
                pairs = pairs + hashmap[tuple(row)]

        return pairs