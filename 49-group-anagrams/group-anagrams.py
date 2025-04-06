class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for each in strs:
            sort_each = ''.join(sorted(each))
            anagrams[sort_each].append(each)
        return list(anagrams.values())

