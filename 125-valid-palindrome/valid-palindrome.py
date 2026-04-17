class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()

        string = ""
        for ch in s.lower():
            if 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57:
                string += ch

        iter = list(string)
        left = 0 
        right = len(iter)-1
        while left<right:
            if iter[left] != iter[right]:
                return False
            left += 1
            right -= 1
        return True