class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        for ch in s1:
            freq_s1[ch] += 1
        print(freq_s1)

        l = 0
        r = len(s1)
        freq_substring = defaultdict(int)
        substring = s2[l : r]
        for ch in substring:
            freq_substring[ch] += 1
        while r < len(s2):
            if freq_substring == freq_s1:
                return True
            freq_substring[s2[l]] -= 1
            if freq_substring[s2[l]] == 0:
                del freq_substring[s2[l]]
            freq_substring[s2[r]] += 1
            l += 1
            r += 1
        if freq_substring == freq_s1:
            return True
        return False
            

        
        
        
        
"""       k = len(s1) 
        freq_substring = defaultdict(int)
        for i in range(len(s2) - k + 1):
            substring = s2[i : i + k]  
            for ch in substring:
                freq_substring[ch] += 1
            if (freq_substring == freq_s1):
                return True
        return False
"""         