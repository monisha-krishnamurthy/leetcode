class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setofS = set()
        length = 0
        i, j = 0, 0
        for j in range(i, len(s)):
            while s[j] in setofS:
                setofS.remove(s[i])
                i += 1
            setofS.add(s[j])
            length = max(length, j-i+1)
        return length

