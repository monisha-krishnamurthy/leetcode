class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        dict_s, dict_t = dict(), dict()
        
        if len(s) != len(t):
            return False

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        for char_s in dict_s:
            if char_s not in dict_t or dict_s[char_s] != dict_t[char_s]:
                return False
        return True