class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        for ch in s1:
            freq_s1[ch] += 1

        l = 0
        r = len(s1) 
        substring = s2[l : r]
        for ch in substring:
            if ch in freq_s1:
                freq_s1[ch] -= 1
        while r < len(s2):
            if all(val == 0 for val in freq_s1.values()):
                return True
            if s2[l] in freq_s1:
                freq_s1[s2[l]] += 1
            if s2[r] in freq_s1:
                freq_s1[s2[r]] -= 1
            l += 1
            r += 1
        if all(val == 0 for val in freq_s1.values()):
            return True
        return False
            

        
        
        
        
