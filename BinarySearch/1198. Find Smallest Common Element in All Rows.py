class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
# method 2 ===========================
        # do a binary search on the first row 
        # check if it exists in every row 
        # m == height of mat | n == width of mat 
        # O(nlogn * mlogn) == O(mnlogn)
    
        
        
# method 1 =========================
        # go down every row, then do an intersection check 
        # return min(intersection)
        # O(M * N)
        prevSet = set(mat[0])
        for i in range(1, len(mat)):
            currentSet = set(mat[i])
            prevSet = currentSet.intersection(prevSet)
            
        
        return -1 if len(prevSet) == 0 else min(prevSet)