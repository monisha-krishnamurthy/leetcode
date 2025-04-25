class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:                 
                    break
                charSet.add(s[j]) 
            max_length = max(max_length, len(charSet))
        return max_length


