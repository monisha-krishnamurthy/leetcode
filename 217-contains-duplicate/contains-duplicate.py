class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1 
            if mapping[num] > 1:
                return True
        return False