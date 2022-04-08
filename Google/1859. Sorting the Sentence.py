class Solution:
    def sortSentence(self, s: str) -> str:
        sentenceArray = s.split(" ")
        newSentence = ["" for x in range(len(sentenceArray))]
      
        for word in sentenceArray:
            index = word[-1]
            print(index, word[:-1])
            
            newSentence[int(index)-1] = word[:-1]
            
        print(newSentence)
        return " ".join(newSentence)