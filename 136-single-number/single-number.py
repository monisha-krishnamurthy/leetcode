class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = dict()
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        for key,val in mapping.items():
            if val == 1:
                return key