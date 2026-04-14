class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [i, mapping[diff]]
            mapping[num] = i