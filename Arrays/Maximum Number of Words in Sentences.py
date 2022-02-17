class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0

                
        for sentence in sentences:
            count = len(sentence.split())
            if count>max:
                max = count
                
                
        return max