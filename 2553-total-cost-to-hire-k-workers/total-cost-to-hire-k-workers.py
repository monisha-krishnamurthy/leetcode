class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1 = []
        heap2 = []
        for index, cost in enumerate(costs[:candidates]):
            heapq.heappush(heap1, (cost, index))
            left_index = index
        for index in range(len(costs)-1, len(costs)-1-candidates, -1):
            heapq.heappush(heap2, (costs[index], index))
            right_index = index
        
        cost = 0
        for i in range(k):
            if len(heap2) < candidates and left_index < right_index - 1:
                    heapq.heappush(heap2, (costs[right_index - 1], right_index - 1))
                    right_index = right_index - 1
            if len(heap1) < candidates and left_index < right_index - 1:
                    heapq.heappush(heap1, (costs[left_index + 1], left_index + 1))
                    left_index = left_index + 1
            
            if len(heap1) == 0:
                ele1 = float('inf')
            else:
                ele1, index1 = heap1[0]
            if len(heap2) == 0:
                ele2 = float('inf')
            else:
                ele2, index2 = heap2[0]
                
            if ele1 > ele2:
                heapq.heappop(heap2)
                cost += ele2
            elif ele2 > ele1:
                heapq.heappop(heap1)
                cost += ele1
                
            else:
                if index1 < index2:
                    heapq.heappop(heap1)
                    cost += ele1
                elif index1 == index2:
                    heapq.heappop(heap1)
                    heapq.heappop(heap2)
                    cost += ele1
        return cost
