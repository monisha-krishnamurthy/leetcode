class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        sorted_dict = sorted(mapping.items(), key=lambda item: item[1], reverse = True)
        return [key for key, val in sorted_dict[:k]]