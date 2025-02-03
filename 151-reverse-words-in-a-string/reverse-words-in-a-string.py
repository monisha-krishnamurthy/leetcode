class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for i in s:
            print(i)
            if i == " ": 
                if word != "":
                    words.append(word)
                    word = ""
            else:
                word += i
        if word != "":
            words.append(word)
        print(words)
        out = ""
        for i in range(len(words)-1, -1, -1):
            out += words[i] + " "
        return out.strip()

        