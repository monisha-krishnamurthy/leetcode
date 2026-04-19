class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapping = [0]*26
        for ch in s1:
            mapping[ord(ch) - ord('a')] += 1

        length = len(s1)
        k = 0
        charset = [0]*26
        substring = s2[k:k+length]
        for m in range(len(substring)):
            charset[ord(substring[m]) -  ord('a')] += 1

        if charset == mapping:
            return True

        i = 0
        for j in range(length, len(s2)):
            charset[ord(s2[i]) - ord('a')] -= 1
            charset[ord(s2[j]) - ord('a')] += 1
            i += 1
            if charset == mapping:
                return True
        return False