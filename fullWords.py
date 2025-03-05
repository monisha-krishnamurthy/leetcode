# 3. Write in full words: (10 Points)
# On legal and financial documents, like cheques, numbers must sometimes be written in full words.
# Example: 283 must be written as two-eight-three. Write a predicate full_words/1 to print (non-
# negative) integer numbers in full words.
# Sample Run:
# ?- full_words(283).
# two-eight-three
# ?- full_words(2018).
# two-zero-one-eight

def full_words(n):
    map = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    l1 = []
    while(n!=0):
        l1.append(n%10)
        n = n//10
    
    string = ""
    for i in l1:
        if i != l1[0]:
            string = map[i] + "-" + string
        else:
            string = map[i] + string
    print(string)

if __name__ == "__main__":
    full_words(283)
