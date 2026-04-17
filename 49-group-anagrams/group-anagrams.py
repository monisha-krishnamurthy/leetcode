class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            mapping[sortedS].append(s)
        return list(mapping.values())
