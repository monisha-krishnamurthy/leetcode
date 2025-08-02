class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
            
        heapq.heapify(maxHeap)
        for i in range(k -1):
            heapq.heappop(maxHeap)
        result = heapq.heappop(maxHeap)
        return result * -1

     