class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        # ord(char):Takes a character and returns its ASCII number.
        # chr(number):Takes an ASCII number and returns its character.
        for ch in s:
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + 32)  # convert uppercase to lowercase
                string += ch
            elif 'a' <= ch <= 'z' or '0' <= ch <= '9':
                string += ch
            # skip non-alphabetic characters

        print(string)
        return string == string[::-1]  # check if string is palindrome