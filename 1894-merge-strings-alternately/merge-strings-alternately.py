class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        final_word = ""
        result = ""

        while(i<len(word1) and i<len(word2)):
            result += word1[i] + word2[i]
            i +=1

        if len(word1)<len(word2):
            final_word = word2[len(word1):]
        else:
            final_word = word1[len(word2):]
            
        return result + final_word
        
        

        