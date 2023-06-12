class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # just trie and dfs will TLE, so we need to do further pruning
        # once we have visited this part of the trie,
        #
        trie = Node()
        for word in words:
            trie.addWord(word)
        res = []
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, cur):

            isVisiting.add((row, col))
            # print('current', row, col, cur.endOfWord)
            flag = False
            if cur.endOfWord:
                res.append(cur.word)
                if len(cur.trie) == 0:
                    del cur
                    flag = True

            if not flag:
                for direction in directions:
                    newx = row + direction[0]
                    newy = col + direction[1]
                    if newx >= 0 and newx <= m - 1 and newy >= 0 and newy <= n - 1 and (
                    newx, newy) not in isVisiting and board[newx][newy] in cur.trie:
                        # print('starting new', newx, newy, board[newx][newy])
                        dfs(newx, newy, cur.trie[board[newx][newy]])
            isVisiting.discard((row, col))
            return

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.trie:
                    isVisiting = set()
                    dfs(i, j, trie.trie[board[i][j]])

        return set(res)


class Node:
    def __init__(self):
        self.trie = {}
        self.endOfWord = False
        self.word = ""

    def addWord(self, word):
        ptr = self
        for char in word:
            if char not in ptr.trie:
                ptr.trie[char] = Node()
            ptr = ptr.trie[char]
        ptr.endOfWord = True
        ptr.word = word
