class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            res.append(numberOf1Bits(num))
            
        return res
            
        
        
def numberOf1Bits(number):
    count = 0
    while number != 0:
        count += number%2
        number = number>>1
    return count