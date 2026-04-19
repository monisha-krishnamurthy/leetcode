class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mappingP = [0]*26
        for ch in p:
            mappingP[ord(ch) - ord('a')] += 1

        substring = s[:len(p)]
        charset = [0]*26
        for ch in substring:
            charset[ord(ch) - ord('a')] += 1
        
        output = []
        if mappingP == charset:
            output.append(0)

        i = 0
        for j in range(len(p), len(s)):
            charset[ord(s[i]) - ord('a')] -= 1
            charset[ord(s[j]) - ord('a')] += 1
            if charset == mappingP:
                output.append(i+1)
            i += 1
        return output