class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)

        heapq.heapify(minHeap)
        count = len(minHeap) - k
        for i in range(count):
            heapq.heappop(minHeap)
        return heapq.heappop(minHeap)