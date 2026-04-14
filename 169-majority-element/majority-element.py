class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = dict()
        for num in nums:
            mapping[num] = mapping.get(num,0) + 1

        return max(mapping, key=mapping.get)
