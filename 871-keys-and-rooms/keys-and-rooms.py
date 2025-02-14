class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        no_of_nodes = len(rooms)
        visited = [False for i in range(no_of_nodes)]
        self.recursive(0, visited, rooms)
        print(visited)
        for ind,val in enumerate(visited):
            if val == False:
                return False
        return True
    
    def recursive(self, source_index, visited, rooms):
        visited[source_index] = True
        neighbors= rooms[source_index]
        print(neighbors)
        for n in neighbors:
            if visited[n] == False:
                self.recursive(n, visited, rooms)
            else:
                continue