class Solution:
    #USING SLIDING WINDOW TECHNIQUE (TWO-POINTER APPROACH)
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freq_dict = defaultdict(int)
        l = 0

        for r in range(len(s)):
            freq_dict[s[r]] += 1

            if (r - l + 1) - max(freq_dict.values()) > k:
                freq_dict[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)
        return maxLength
#TIME-COMPLEXITY: O(n)
#SPACE-COMPLEXITY: O(m)




 
