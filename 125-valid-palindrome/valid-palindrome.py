class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        inter = []
        for char in s:
            if 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
                inter.append(char)
        string = "".join(inter)

        string = list(string)
        if len(string) == 1:
            return True

        i, j = 0, len(string)-1
        while i <= j:        
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True