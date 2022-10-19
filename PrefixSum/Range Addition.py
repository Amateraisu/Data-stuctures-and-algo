class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # [start, end , val ]
        
        prefix = [0] * (length + 2)
        
        
        for update in updates:
            start, end, incrementValue = update 
            
            prefix[start + 1] += incrementValue 
            prefix[end + 2] -= incrementValue 
            
        res = [0] * length
        current = 0 
        for i in range(1, len(prefix) - 1):
            current += prefix[i]
            res[i - 1] = current
            
        return res
        