class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # O(n) time complexity and O(n) space complexity 
        # [1,0,2,1]
        
        # [1,2,3] , 1
        
        # 1 xor 0 = 1 
        # 1 xor 1 = 0
        
        # 1 xor 0 = 1 
        # 0 xor 2 = 2 
        # 2 xor 1 = 3
        
        # 2 xor 3 = 1
        # 01 xor 11 = 2 
        
        # 1 xor 1 = 1 res = [1]
        
        #  
        
        original = [first]
        for index in range(len(encoded)):
            number = encoded[index]
            original.append(number ^ original[index])
            
        return original