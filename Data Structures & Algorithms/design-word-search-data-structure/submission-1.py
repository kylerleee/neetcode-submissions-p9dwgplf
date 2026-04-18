class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        copy = self.root
        for c in word:
            if c not in copy.children:
                copy.children[c] = TrieNode()
            copy = copy.children[c]
        copy.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            copy = root

            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in copy.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] in copy.children:
                        copy = copy.children[word[i]]
                    else:
                        return False
            return copy.endOfWord
        
        return dfs(0, self.root)
