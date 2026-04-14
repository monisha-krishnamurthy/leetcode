class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setN = set(nums)
        i = 0
        while i <= len(nums):
            if i not in setN:
                return i
            i += 1