class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict() vs defaultdict(): explicit control over missing keys Vs cleaner code w/o manual checks
        mapping = defaultdict(int) 

        for char in s:
            mapping[ord(char) - ord('a')] += 1
        
        for char in t:
            mapping[ord(char) - ord('a')] -= 1

        for values in mapping.values():
            if values != 0:
                return False
        return True