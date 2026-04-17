class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()

        string = ""
        for ch in s.lower():
            if 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57:
                string += ch

        left = 0 
        right = len(string)-1
        while left<right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True