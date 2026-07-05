class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            c = ord(i) - ord("a")
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            c = ord(i)-ord("a")
            if cur.children[c] == None:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            c = ord(i)-ord("a")
            if cur.children[c] == None:
                return False
            cur = cur.children[c]
        return True

        
        