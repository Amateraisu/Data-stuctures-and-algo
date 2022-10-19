from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # bucket sort + trie 
        # O(N) time since the number of words are a constant factor 
        n = len(words)
        cnt = Counter(words)
        bucket = [{} for _ in range(n+1)]
        self.k = k

        def add_word(trie: Mapping, word: str) -> None:
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
            root['#'] = {}

        def get_words(trie: Mapping, prefix: str) -> List[str]:
            if self.k == 0:
                return []
            res = []
            if '#' in trie:
                self.k -= 1
                res.append(prefix)
            for i in range(26):
                c = chr(ord('a') + i)
                if c in trie:
                    res += get_words(trie[c], prefix+c)
            return res

        for word, freq in cnt.items():
            add_word(bucket[freq], word)

        res = []
        for i in range(n, 0, -1):
            if self.k == 0:
                return res
            if bucket[i]:
                res += get_words(bucket[i], '')
        return res
        
        
        
        
        
        # Time complexity: Nlog(N) where N is the number of unique keys in the dictionary
        
#         frequencies = Counter(words)
        
#         array = []
        
#         for word, count in frequencies.items():
#             print(word, count)
#             array.append([count, word])
            
#         array.sort(key = lambda x: ( - 1 * x[0], x[1]))
        
        
#         return [arra[1] for arra in array[:k]]