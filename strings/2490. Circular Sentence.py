class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # the last character of a word is equals to the first character of the next word 
        # the last character of the last word is equals to the first character of the first word 
        splitted = sentence.split(" ")

        for i, word in enumerate(splitted):

            if i == len(splitted)-1:
                if word[-1] != splitted[0][0]:
                    return False 
                
            else:
                if word[-1] != splitted[i + 1][0]:
                    return False
                
        return True 