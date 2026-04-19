class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = defaultdict(int)
        maxlength = 0
        i, j = 0, 0
        for j in range(len(s)):
            mapping[s[j]] += 1
            length = j-i+1
            maxFreq = max(mapping.values())
            if length > maxFreq+k:
                mapping[s[i]] -= 1
                i += 1
            maxlength = max(j-i+1, maxlength)
        return maxlength