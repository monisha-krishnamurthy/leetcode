class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) < len(word2):
            final_len = len(word1)
            final_word = word2[final_len:]
        else:
            final_len = len(word2)
            final_word = word1[final_len:]
        for i in range(final_len):
            result += word1[i] + word2[i]
        result += final_word
        return result
        
        

        