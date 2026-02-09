class Solution:
    #flyod warshall algo
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float("inf")
        mat = [[inf] * n for _ in range(n)]

        for u,v,w in times:
            mat[u-1][v-1] = w
        for i in range(n):
            mat[i][i] = 0

        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][mid] + mat[mid][j])

        res = max(mat[k-1])
        return res if res < inf else -1





