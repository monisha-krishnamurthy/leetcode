class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # USING HASH-SET
        numSet = set(nums)
        longestSeq = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longestSeq = max(length, longestSeq)
        return longestSeq

# TIME-COMPLEXITY : O(n)
# SPACE-COMPLEXITY: O(n) 
        # numSet = set(nums)
        # longest = 0

        # for num in numSet:
        #     if (num - 1) not in numSet:
        #         length = 1
        #         while (num + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        # return longest
# [~~~~~~tricky problem, solve multiple times~~~~~~~~~~~~~~]