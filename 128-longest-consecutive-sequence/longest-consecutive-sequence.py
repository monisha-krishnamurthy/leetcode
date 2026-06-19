class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        set_nums = set(nums)
        for num in set_nums:
            if num-1 not in set_nums:
                longest = 1
                while num+longest in set_nums:
                    longest += 1
                length = max(length, longest)
        return length