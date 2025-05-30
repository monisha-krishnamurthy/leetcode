class TrieNode:
    def __init__(self):
        self.children = {}
        self.isAWord = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root 
        for ch in word:
            if ch in node.children:
                node = node.children[ch] 
            else:
                node.children[ch] = TrieNode() 
                node = node.children[ch] 
        node.isAWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.isAWord 

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)