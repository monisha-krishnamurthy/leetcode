class Solution:
    #USING SLIDING WINDOW (TWO-POINTERS)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) 
            max_length = max(max_length, r - l + 1)
        return max_length


#TIME-COMPLEXITY: O(n*m) where m is the total no. of unique chars in the array
#SPACE-COMPLEXITY: O(m)

