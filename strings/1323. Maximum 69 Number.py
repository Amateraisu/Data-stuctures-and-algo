class Solution:
    def maximum69Number (self, num: int) -> int:
        stringify = str(num)
        
        res = []
        count = 1 
        for char in stringify:
            if char == "6" and count > 0:
                res.append("9")
                count -= 1 
            else:
                res.append(char)
        final = int("".join(res))
        
        
        return final