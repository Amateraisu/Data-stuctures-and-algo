class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        # so 
        # first go 
        palinList = list(palindrome)
        
        # make smaller 
        for index ,char in enumerate(palindrome):
            if char != "a":
                print(char, index)
                if len(palindrome) % 2 != 0 and index == (len(palindrome) - 1) / 2:
                    pass 

                else: # it is an odd and I can replace anything I like 
                    # always make it the smallest 
                    # so I can always make it an a 
                    palinList[index] = "a"
                    return "".join(palinList)
                
        
        # make bigger section 
        # if I had come across this part, that means 
        
        # 1. everything was an a 
        # 2. everything was an A, except the middle char which didnt matter, 
        # 
        palinList[-1] = chr(ord(palinList[-1]) + 1)
        
        return "".join(palinList)