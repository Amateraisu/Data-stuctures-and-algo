class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        c = Counter(letters)
        # technically there are only 26 letters, so this should be constant time
        res = 0
        maps = [Counter(x) for x in words]

        n = len(words)
        def dfs(i, cur):
            nonlocal res
            if i == n:
                res = max(res,cur )
                return
            # should make
            can = True
            for ch in maps[i]:

                if maps[i][ch] > c[ch]:
                    can = False
            if can:
                s = 0
                for ch in maps[i]:
                    s += maps[i][ch] * score[ord(ch) - ord('a')]
                    c[ch] -= maps[i][ch]
                dfs(i + 1, cur + s)
                for ch in maps[i]:
                    c[ch] += maps[i][ch]
            # should not make
            dfs(i + 1, cur)
            return

        dfs(0, 0)

        return res