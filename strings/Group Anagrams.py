from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for word in words:
            sortedOrder = "".join(sorted(word))

            myDict[sortedOrder].append(word)
            
        return myDict.values()