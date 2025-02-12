import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
         
        for i in range(len(nums)-k):
            heapq.heappop(heap)

        return heap[0]