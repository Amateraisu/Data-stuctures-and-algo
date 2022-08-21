class Solution:
    def decodeString(self, s: str) -> str:
        
        
        return decodeStringHelper(s)
    
    
    
    
def decodeStringHelper(string):

    res = []
    index = 0 
    
    while index < len(string):
        currentCharacter = string[index]

        stringToAdd = currentCharacter 
        if currentCharacter.isnumeric():

            number, newIndex = findNumber(string, index)
            nextPtrPosition = findNextPosition(string, newIndex + 1)
            
   
            stringToAdd = number * decodeStringHelper(string[newIndex + 1: nextPtrPosition - 1])

            stringToAdd = "".join(stringToAdd)
            index = nextPtrPosition
        else:
            index += 1 
            
            
        
        res.append(stringToAdd)

        
        
    return "".join(res) 

def findNumber(string, index):
    res = []
    currentCharacter = string[index]
    
    while currentCharacter != "[":
        
        res.append(currentCharacter)
        index += 1 
        currentCharacter = string[index]
        
    return [int("".join(res)), index]
        


def findNextPosition(string, startingIndex):

    
    numberOfOpen = 1
    while numberOfOpen > 0:
        currentCharacter = string[startingIndex]

        if currentCharacter == "]":
            numberOfOpen -=1
        elif currentCharacter == "[":
            numberOfOpen += 1 
            
        startingIndex += 1 
        
    
    return startingIndex