class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n+1)]

        def dfs(node, parent):
            if visited[node]:
                return True

            visited[node] = True
            for neigh in adj_list[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            return False 

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            visited = [False] * (n+1)

            if dfs(u, -1):
                return [u,v]
        return []

