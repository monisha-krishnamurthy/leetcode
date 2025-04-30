class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_s = [0]*128
        freq_t = [0]*128

        for ch in t:
            freq_t[ord(ch)] += 1

        l = 0
        minLength = len(s) + 1
        start = 0
        for r in range(len(s)):
            freq_s[ord(s[r])] += 1
            while self.match_arrays(freq_s, freq_t):
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start = l
                freq_s[ord(s[l])] -= 1
                l += 1
                
        return "" if minLength > len(s) else s[start: start + minLength]

    def match_arrays(self, arr1, arr2):
        for i in range(len(arr2)):
            if arr2[i] == 0:
                continue 
            if arr1[i] >= arr2[i]:
                continue
            else:
                return False 
        return True