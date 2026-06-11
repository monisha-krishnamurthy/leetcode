class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for string in strs:
            sorted_string = sorted(string)
            mapping[''.join(sorted_string)].append(string)
        output = []
        print(mapping.values())
        for values in mapping.values():
            output.append(values)
        return output 


