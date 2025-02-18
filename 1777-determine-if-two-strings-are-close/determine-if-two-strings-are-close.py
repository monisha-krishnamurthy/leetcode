class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        word1_dict = dict()
        word2_dict = dict()
        for ch in list(word1):
            if ch in word1_dict:
                word1_dict[ch] +=1
            else:
                word1_dict[ch] = 1
        for ch in list(word2):
            if ch in word2_dict:
                word2_dict[ch] +=1
            else:
                word2_dict[ch] = 1
        # print(word1_dict, word2_dict)

        if sorted(list(word1_dict.values()))== sorted(list(word2_dict.values())):
            return True
        return False