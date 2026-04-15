class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            charArray = [0]*26
            for ch in s:
                charArray[ord(ch) - ord('a')] += 1
            mapping[tuple(charArray)].append(s) 
        return list(mapping.values())

