class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for string in strs:
            sortedS = ''.join(sorted(string))
            mapping[sortedS].append(string)
        return list(mapping.values())

