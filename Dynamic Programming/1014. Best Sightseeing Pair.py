class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        arrayI = [0 for num in values]
        arrayJ = [0 for num in values]
        
        arrayI[0] = values[0]
        res = float("-inf")
        for num in range(1,len(arrayI)):
            arrayI[num] = max(values[num]+num, arrayI[num-1])
            
        for num in range(1,len(arrayJ)):
            
            value2 = values[num] - num
            arrayJ[num] = value2
            res = max(res, value2 + arrayI[num-1])
            
        print(arrayI)
        print(arrayJ)
        return res