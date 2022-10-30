class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (x[0], -x[1]))

        res = 0 
        greatestDefSoFar = float("-inf")
        
        for i in range(len(properties) - 1, -1, -1):
            attack, defence = properties[i]
            if defence < greatestDefSoFar:
                res += 1 
            greatestDefSoFar = max(greatestDefSoFar, defence)
            

                
                
        return res 