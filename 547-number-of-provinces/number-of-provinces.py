class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for i in range(len(isConnected))]
        no_of_provinces = 0

        for i in range(len(isConnected)):
            if(visited[i] == False):
                self.recursive(i, visited, isConnected)
                no_of_provinces +=1
        return no_of_provinces

    def recursive(self, i, visited, isConnected):
        visited[i] = True
        for j in range(len(isConnected[i])):
            if(isConnected[i][j] == 1 and i!=j):
                if(visited[j] == False):
                    self.recursive(j, visited, isConnected)    