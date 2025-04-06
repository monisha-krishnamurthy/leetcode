class Solution:
    import heapq
    # USING FREQ MAP
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] +=1

        heap = list()
        for key,val in freq_map.items():
            heapq.heappush(heap, (-val, key))
        print(heap)

        output = list()
        for i in range(k):
            freq, num = heapq.heappop(heap)
            output.append(num)
        return output
