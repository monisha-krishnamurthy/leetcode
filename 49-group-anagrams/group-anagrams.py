class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            charSet = [0]*26
            for ch in s:
                charSet[ord(ch)-ord('a')] += 1
            mapping[tuple(charSet)].append(s)
        return list(mapping.values())

