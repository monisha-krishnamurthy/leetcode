class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        s = list(s)
        initial_vowels= 0
        for i in range(k):
            if s[i] in vowels:
                initial_vowels +=1
        print(initial_vowels)

        left= 0
        right= k-1
        final_vowels = initial_vowels
        while(right < len(s)-1):
            right +=1 
            if s[left] in vowels and s[right] in vowels:
                initial_vowels = initial_vowels
            elif s[left] in vowels and s[right] not in vowels:
                initial_vowels -=1
            elif s[left] not in vowels and s[right] in vowels:
                initial_vowels += 1
            else:
                initial_vowels = initial_vowels
            final_vowels = max(initial_vowels, final_vowels)
            left +=1
        return final_vowels
        
