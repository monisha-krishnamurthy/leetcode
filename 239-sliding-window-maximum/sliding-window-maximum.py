import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #USING HEAPS
        result = list()

        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result.append(-heap[0][0]) 

        for i in range(1, len(nums) - k + 1):
            #print(i, -nums[i-1], heap)
            #if -heap[0][0] == nums[i-1]:
            #    heapq.heappop(heap) 
            heapq.heappush(heap, (-nums[i+k-1], i+k-1))
            while heap[0][1] < i:
                heapq.heappop(heap) 
            result.append(-heap[0][0]) 
        return result
#TIME-COMPLEXITY: O(n^2) 
#SPACE-COMPLEXITY: O(n-k+1+k) = )(n+1) i.e., the no. of windows 


