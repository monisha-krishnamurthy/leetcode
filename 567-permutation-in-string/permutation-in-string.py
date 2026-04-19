class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapping = [0]*26
        for ch in s1:
            mapping[ord(ch) - ord('a')] += 1

        length = len(s1)
        i = 0
        while i <= len(s2)-length:
            charset = [0]*26
            substring = s2[i:i+length]
            for k in range(len(substring)):
                charset[ord(substring[k]) -  ord('a')] += 1
            if charset == mapping:
                return True
            else:
                i += 1
        return False