class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res += word.split(separator)
        res = [l for l in res if l != ""]
        return res