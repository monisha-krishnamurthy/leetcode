class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = dict()

        for i in prerequisites:
            node = i[0]
            neighbor = i[1] 
            if node not in adj_list:
                adj_list[node] = [neighbor]
            else:
                adj_list[node].append(neighbor)
            if neighbor not in adj_list:
                adj_list[neighbor] = [] 
        print(adj_list)
        
        visited = set()
        recstack = set()

        for i in adj_list:
            if i not in visited and self.recursive(i, adj_list, visited, recstack):
                return False
        return True
    
    def recursive(self, node, adj_list, visited, recstack):
        visited.add(node)
        recstack.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                if self.recursive(neighbor, adj_list, visited, recstack):
                    return True
            elif neighbor in recstack:
                return True
    
        recstack.remove(node)
        return False