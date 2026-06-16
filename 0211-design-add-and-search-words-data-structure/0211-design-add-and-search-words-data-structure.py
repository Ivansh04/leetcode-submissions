class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.is_end=True

    def search(self, word: str) -> bool:
        def dfs(curr,word):
            
          for i,c in enumerate(word):
            if c != '.' and c not in curr.children:
                return False
            if c=='.':
                rest = word[i + 1:]
                
                for key in curr.children.values():
                    if dfs(key,rest):
                        return True
                return False
            curr=curr.children[c]
          return curr.is_end
 

        return dfs(self.root,word)
        
