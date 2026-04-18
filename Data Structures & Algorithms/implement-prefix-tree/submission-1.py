class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        copy = self.root
        for i in range(len(word)):
            if not word[i] in copy.children:
                copy.children[word[i]] = TrieNode()
            copy = copy.children[word[i]]
            if i == len(word) - 1:
                copy.endOfWord = True

    def search(self, word: str) -> bool:
        copy = self.root
        for i in range(len(word)):
            if word[i] in copy.children:
                copy = copy.children[word[i]]
        
        return copy.endOfWord
                

    def startsWith(self, prefix: str) -> bool:
        copy = self.root
        for i in range(len(prefix)):
            if prefix[i] in copy.children:
                copy = copy.children[prefix[i]]
            else:
                return False
        
        return True
        