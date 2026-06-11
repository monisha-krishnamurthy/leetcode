class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping = defaultdict(int)
        for num in nums:
            freq_mapping[num] += 1

        heap = list()
        for key, val in freq_mapping.items():
            heapq.heappush(heap, (-val, key))

        output = []
        while k > 0:
            freq, num = heapq.heappop(heap)
            output.append(num)
            k -=1
        return output


