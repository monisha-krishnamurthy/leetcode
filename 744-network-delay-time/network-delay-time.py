class Solution:
    #djikstra's algo
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))

        minHeap = [(0,k)]
        visit = set()
        res = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = weight

            for n1, w1 in adj[node]:
                if n1 not in visit:
                    heapq.heappush(minHeap, (w1+weight, n1))
        return res if len(visit) == n else -1

