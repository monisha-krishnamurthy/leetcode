class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)
        
        def find(u):
            while u != parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False

            if rank[pu] > rank[pv]:
                parent[pu] = pv
                rank[pv] += rank[pu]
            else:
                parent[pv] = pu
                rank[pu] += rank[pv]
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]


