class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        output = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                output.append(mapping[diff])
                output.append(i)
            mapping[num] = i
        return output