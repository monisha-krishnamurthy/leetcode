class TrieNode:
    def __init__(self):
        self.children = {}
        self.isAWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch] 
            else:
                node.children[ch] = TrieNode() 
                node = node.children[ch] 
        node.isAWord = True

    def search(self, word: str) -> bool:
        
        def recursive(index: int, word: str, node: TrieNode):
            if index >= len(word):
                return node.isAWord
            ch = word[index]
            if ch == ".":
                for each in node.children:
                    if recursive(index+1, word, node.children[each]) == True:
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                else:                
                    node = node.children[ch] 

            return recursive(index+1, word, node)        

        return recursive(0, word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)