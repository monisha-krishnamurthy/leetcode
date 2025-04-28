class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        for ch in s1:
            freq_s1[ch] += 1

        k = len(s1)
        substring = s2[0 : k]
        for ch in substring:
            if ch in freq_s1:
                freq_s1[ch] -= 1

        for r in range(len(s1), len(s2)):
            if all(val == 0 for val in freq_s1.values()):
                return True
            if s2[r - k] in freq_s1:
                freq_s1[s2[r - k]] += 1
            if s2[r] in freq_s1:
                freq_s1[s2[r]] -= 1
        if all(val == 0 for val in freq_s1.values()):
            return True
        return False
            

        
        
        
        
