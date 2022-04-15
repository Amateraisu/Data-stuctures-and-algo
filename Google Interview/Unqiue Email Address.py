class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #im given a list of strings containing emails 
        
        #in the localname, everything after the + sign is ignored 
        # my job is to check for unique emails. 
        
        # so the first thing that comes to mind is probably a set 
        
        mySet = set()
        for email in emails:
            actualAddress = forwardedEmailAddress(email)
            if actualAddress not in mySet:
                mySet.add(actualAddress)
        return len(mySet)
        
        
        
def forwardedEmailAddress(email):
    finalAddress = ""
    localName, domainName = email.split('@')
    for charIndex in range(len(localName)):
        char = localName[charIndex]
        if char ==".":
            continue
        elif char =="+":
            break
        finalAddress += char
    finalEmailAddress = finalAddress + "@" + domainName
    
        
    
    return finalEmailAddress