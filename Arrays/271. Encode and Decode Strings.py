class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for string in strs:
            lengthOfString = len(string)
            res = res+str(lengthOfString)+ '#' + string
        return res
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ptr1 = 0 
        result = []

        while ptr1 < len(s):
            # read the number of chars
            j = ptr1
            while s[j] != '#':
                j+=1
            length = int(s[ptr1:j])
            res = ""
     
            result.append(s[j+1:j+1+length])
            

            ptr1 = j+1+length
            
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs)