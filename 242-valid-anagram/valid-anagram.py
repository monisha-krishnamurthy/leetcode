class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_S = defaultdict(int)
        for ch in s:
            mapping_S[ch] += 1
        for ch in t:
            mapping_S[ch] -= 1
        print(mapping_S)
        for i in mapping_S.values():
            if i != 0:
                return False
        return True
