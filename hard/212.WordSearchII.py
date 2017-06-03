"""
思路：Trie+dfs
"""
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
    #     words = list(set(words))
    #     if len(board)==0 or len(board[0]) == 0:return []
    #     res = []
    #     for word in words:
    #         find = False
    #         for i in range(len(board)):
    #             if find:break
    #             for j in range(len(board[0])):
    #                 if board[i][j] == word[0]:
    #                     used = [[False] * len(board[0]) for _ in range(len(board))]
    #                     if self.find(board,used,word,i,j):
    #                         res.append(word)
    #                         find = True
    #                         break
    #     return res
        
    # def find(self,board,used,word,i,j):
    #     print i,j,word
    #     res = False
    #     word = word[1:]
    #     if word=='':
    #         return True
    #     used[i][j] = True
    #     if i-1>=0 and not used[i-1][j] and board[i-1][j] == word[0]:
    #         res |= self.find(board,used,word,i-1,j)
    #     if j+1<len(board[0]) and not used[i][j+1] and board[i][j+1] == word[0]:
    #         res |= self.find(board,used,word,i,j+1)
    #     if i+1<len(board) and not used[i+1][j] and board[i+1][j] == word[0]:
    #         res |= self.find(board,used,word,i+1,j)
    #     if j-1>=0 and not used[i][j-1] and board[i][j-1] == word[0]:
    #         res |= self.find(board,used,word,i,j-1)
    #     return res
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
            
        
