class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        fullString = restoreString(s)
        finalKey = generateKey(fullString,k)
        
        return finalKey
    
    
def restoreString(string):
    finalAnswer = ""
    listOfChars = string.split("-")
    fullString = "".join(listOfChars)
    return fullString

def generateKey(string,key):
    string = string.upper()
    res = ""
    listVersion = list(string)
    ptr1 = len(listVersion)-key
    while ptr1 > 0:
        listVersion.insert(ptr1,"-")
        ptr1 -=key
    return "".join(listVersion)