class Solution:
    #USING SLIDING WINDOW TECHNIQUE + HASH-MAP 
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t, window = defaultdict(int), defaultdict(int)
        for ch in t:
            freq_t[ch] += 1
        print(freq_t)

        need, have = len(freq_t), 0
        l = 0
        minLength, minIndex = float("inf"), [-1, -1]
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in freq_t and window[ch] == freq_t[ch]:
                have += 1
            
            while need == have:
                if (r - l + 1) < minLength:
                    minIndex = [l, r]                    
                    minLength = r - l + 1
                window[s[l]] -= 1 
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        l, r = minIndex
        return s[l : r + 1] if minLength < float("infinity") else ""

#TIME-COMPLEXITY: O(N)
#SPACE-COMPLEXITY: O(M)
