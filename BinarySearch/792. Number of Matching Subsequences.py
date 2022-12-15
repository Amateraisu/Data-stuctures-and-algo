from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0 
        mapper = defaultdict(list)
        for i, char in enumerate(s):
            mapper[char].append(i)

        def isSubsequence(word):
            prev = -1
            for char in word:
                if char not in mapper:
                    return False 

                index = bisect_right(mapper[char], prev)

                if index == len(mapper[char]):
                    return False
                prev = mapper[char][index]

            return True

        # every char is already sorted 
        for word in words:
            if isSubsequence(word):
                res += 1 

        return res 