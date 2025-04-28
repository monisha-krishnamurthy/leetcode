class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        for ch in s1:
            freq_s1[ch] += 1

        k = len(s1) 
        for i in range(len(s2) - k + 1):
            freq_substring = defaultdict(int)
            substring = s2[i : i + k]  
            for ch in substring:
                freq_substring[ch] += 1
            if (freq_substring == freq_s1):
                return True
        return False
            