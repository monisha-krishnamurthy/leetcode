class Solution:
    import heapq
    # USING FREQ MAP & MAX-HEAP
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] +=1

        heap = list()
        for key,val in freq_map.items():
            # push elements with max value first to arrange from high to low
            # if not, will arrange from low to high because by default it is a min-heap
            heapq.heappush(heap, (-val, key))

        output = list()
        for i in range(k):
            freq, num = heapq.heappop(heap)
            output.append(num)
        return output
