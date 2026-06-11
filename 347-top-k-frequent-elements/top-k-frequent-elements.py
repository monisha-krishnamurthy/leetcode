class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping = defaultdict(int)
        for num in nums:
            freq_mapping[num] += 1
        sorted_list = sorted(freq_mapping.items(), key=lambda x:x[1], reverse = True) 
        output = []
        for i in range(k):
            output.append(sorted_list[i][0])
        return output
