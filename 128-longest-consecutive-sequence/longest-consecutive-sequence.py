class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numbers = set(nums)
        for num in numbers:
            length = 0
            if num-1 not in numbers:
                while num+length in numbers:
                    length += 1
            longest = max(length, longest)
        return longest
       